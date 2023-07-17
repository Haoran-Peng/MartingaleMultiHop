import numpy as np
import math
import pandas as pd
import os

def analyze(urllc_markov_mat, urllc_resource_block, urllc_process_num,
            embb_markov_mat, embb_resource_block, embb_process_num,
            service_markov_mat, service_resources_block, edf_param, time_slot, case_name, scenario_name):

    max_theta1 = S1_param(urllc_markov_mat, urllc_resource_block, urllc_process_num,
                          embb_markov_mat, embb_resource_block, embb_process_num,
                          service_markov_mat, service_resources_block)

    max_theta2 = S2_param(urllc_markov_mat, urllc_resource_block,
                          urllc_process_num, service_markov_mat,
                          service_resources_block)

    FIFO(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block,
         embb_process_num, service_markov_mat, service_resources_block, time_slot, case_name,scenario_name)

    SP_URLLC(max_theta2, urllc_markov_mat, urllc_resource_block, urllc_process_num, service_markov_mat,
             service_resources_block, time_slot, case_name,scenario_name)

    SP_eMBB(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block,
            embb_process_num, service_markov_mat, service_resources_block, time_slot, case_name,scenario_name)

    EDF_URLLC(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat,
              embb_resource_block, embb_process_num,
              service_markov_mat, service_resources_block, max_theta2, edf_param, time_slot, case_name,scenario_name)
    """ SP case 當urllc之服務比較高"""

    EDF_eMBB(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
             embb_markov_mat, embb_resource_block, embb_process_num,
             service_markov_mat, service_resources_block, edf_param, time_slot, case_name,scenario_name)

    Backlog(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block, embb_process_num,
            service_markov_mat, service_resources_block, case_name,scenario_name)


def Backlog(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block, embb_process_num, service_markov_mat, service_resource_block, case_name,scenario_name):
    """ FIFO case 抓Ks中的比例"""
    delay_label = []
    for i in range(5555):
        delay_label.append(i * 32 / 1000)
    delay = np.ones(5555)
    # for i in range(0, 5555, 1):
    #     probability = (math.exp(1) * sv_rate / (sv_rate - tc_rate - eb_rate)) * (math.exp(-theta * ((i))))
    #     delay_URLLC[i] = probability
    for i in range(0, 5555, 1):
        probability = findminBacklog(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                     embb_markov_mat, embb_resource_block, embb_process_num,
                                     service_markov_mat, service_resource_block, i)
        # probability = (math.exp(1) * sv_rate / (sv_rate - tc_rate - eb_rate)) * (math.exp(-theta * ((i))))
        delay[i] = probability

    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/BACKLOG.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/BACKLOG.xlsx')
    writer.close()
    return None


def findminBacklog(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_process_num, embb_resource_block, service_markov_mat, service_resource_block, i):
    betas = np.arange(0.001, max_theta1, 0.0001)
    min_z = 1
    for beta in betas:
        urllc_s = (math.log(urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(service_markov_mat[0][1] * math.exp(-beta * service_resource_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s - embb_process_num * embb_s)) * (math.exp(-beta * i))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def EDF_eMBB(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
             embb_markov_mat, embb_resource_block, embb_process_num,
             service_markov_mat, service_resources_block, edf_param, time_slot, case_name,scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        if i >= edf_param:
            probability = findminEDF_eMBB1(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                           embb_markov_mat, embb_resource_block, embb_process_num,
                                           service_markov_mat, service_resources_block, i, edf_param)
        else:
            probability = findminEDF_eMBB2(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                           embb_markov_mat, embb_resource_block, embb_process_num,
                                           service_markov_mat, service_resources_block, i, edf_param)
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/EDF_eMBB.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/EDF_eMBB.xlsx')
    writer.close()
    return None


def findminEDF_eMBB1(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                     embb_markov_mat, embb_resource_block, embb_process_num,
                     service_markov_mat, service_resources_block, i, edf_param):
    betas = np.arange(0.001, max_theta1, 0.0001)
    min_z = 1
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resources_block) + service_markov_mat[0][0])) / -beta

        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s - embb_process_num * embb_s)) * (
            math.exp(-beta * (i * service_s - edf_param * urllc_process_num * urllc_s)))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def findminEDF_eMBB2(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                     embb_markov_mat, embb_resource_block, embb_process_num,
                     service_markov_mat, service_resources_block, i, edf_param):
    betas = np.arange(0.001, max_theta1, 0.0001)
    min_z = 1
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resources_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s - embb_process_num * embb_s)) * math.exp(-beta * (i * (service_s - urllc_process_num * urllc_s)))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def findminEDF_URLLC2(max_theta2, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                      service_markov_mat, service_resource_block, edf_param, i):
    betas = np.arange(2, max_theta2, 0.01)
    min_z = 1
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resource_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s)) * (
            math.exp(-beta * i * service_s))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def findminEDF_URLLC1(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                      embb_markov_mat, embb_resource_block, embb_process_num, service_markov_mat,
                      service_resource_block, edf_param, i):
    betas = np.arange(0.001, max_theta1, 0.0001)
    min_z = 100
    for beta in betas:
        urllc_s = (math.log(urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(service_markov_mat[0][1] * math.exp(-beta * service_resource_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s - embb_process_num * embb_s)) * (
            math.exp(-beta * (i * service_s + edf_param * embb_s * embb_process_num)))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def EDF_URLLC(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat,
              embb_resource_block, embb_process_num,
              service_markov_mat, service_resources_block, max_theta2, edf_param, time_slot, case_name,scenario_name):
    delay = np.zeros(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = findminEDF_URLLC1(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                        embb_markov_mat, embb_resource_block, embb_process_num, service_markov_mat,
                                        service_resources_block, edf_param, i) + \
                      findminEDF_URLLC2(max_theta2, urllc_markov_mat, urllc_resource_block,
                                        urllc_process_num, service_markov_mat, service_resources_block, edf_param, i)
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/EDF_URLLC.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/EDF_URLLC.xlsx')
    writer.close()
    return None


def findminSP_eMBB(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                   embb_markov_mat, embb_resource_block, embb_process_num,
                   service_markov_mat, service_resource_block, i):
    betas = np.arange(0.001, max_theta1, 0.0001)
    min_z = 1
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resource_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s - embb_process_num * embb_s)) * (
            math.exp(-beta * (i * (service_s - urllc_process_num * urllc_s))))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def SP_eMBB(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block,
            embb_process_num, service_markov_mat, service_resources_block, time_slot, case_name,scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = findminSP_eMBB(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                     embb_markov_mat, embb_resource_block, embb_process_num,
                                     service_markov_mat, service_resources_block, i)
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/SP_eMBB.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/SP_eMBB.xlsx')
    writer.close()
    return None


def findminSP_URLLC(max_theta2, urllc_markov_mat, urllc_resource_block, urllc_process_num, service_markov_mat,
                    service_resource_block, i):
    betas = np.arange(2, max_theta2, 0.01)
    min_z = 1
    for beta in betas:
        tc_rate = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        sv_rate = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resource_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * sv_rate / (sv_rate - urllc_process_num * tc_rate)) * (math.exp(-beta * (i * sv_rate)))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def SP_URLLC(max_theta2, urllc_markov_mat, urllc_resource_block, urllc_process_num, service_markov_mat,
             service_resource_block, time_slot,
             case_name,scenario_name):
    delay = np.zeros(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = findminSP_URLLC(max_theta2, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                      service_markov_mat,
                                      service_resource_block, i)
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/SP_URLLC.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/SP_URLLC.xlsx')
    writer.close()
    return None


def findminFIFO(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                embb_markov_mat, embb_resource_block, embb_process_num,
                service_markov_mat, service_resource_block, i):
    betas = np.arange(0.001, max_theta1, 0.0001)
    min_z = 1
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resource_block) + service_markov_mat[0][0])) / -beta
        prob = (math.exp(1) * service_s / (service_s - urllc_process_num * urllc_s - embb_process_num * embb_s)) * (
            math.exp(-beta * (i * service_s)))
        if prob < 0:
            break
        if prob < min_z:
            min_z = prob
    return min_z


def FIFO(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
         embb_markov_mat, embb_resource_block, embb_process_num, service_markov_mat, service_resource_block, time_slot,
         case_name,scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)

    for i in range(0, 4000, 1):
        probability = findminFIFO(max_theta1, urllc_markov_mat, urllc_resource_block, urllc_process_num,
                                  embb_markov_mat, embb_resource_block, embb_process_num,
                                  service_markov_mat, service_resource_block, i)
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/FIFO_BOTH.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/SNC/1hop/' + case_name + '/FIFO_BOTH.xlsx')
    writer.close()
    return None


def S1_param(urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block,
             embb_process_num, service_markov_mat, service_resources_block):
    betas = np.arange(0.001, 1, 0.00001)
    error_list = []
    max_z = 0
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        embb_s = (math.log(embb_markov_mat[0][1] * math.exp(beta * embb_resource_block) + embb_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resources_block) + service_markov_mat[0][0])) / -beta
        error = service_s - urllc_process_num * urllc_s - embb_process_num * embb_s
        error_list.append(error)
        if error > 0:
            max_z = beta
        else:
            break
    urllc_s = (math.log(
        urllc_markov_mat[0][1] * math.exp(max_z * urllc_resource_block) + urllc_markov_mat[0][0])) / max_z
    embb_s = (math.log(embb_markov_mat[0][1] * math.exp(max_z * embb_resource_block) + embb_markov_mat[0][0])) / max_z
    service_s = (math.log(
        service_markov_mat[0][1] * math.exp(-max_z * service_resources_block) + service_markov_mat[0][0])) / -max_z
    # print(urllc_process_num * urllc_s, embb_process_num*embb_s, service_s)
    # print(max_z)
    return max_z


def S2_param(urllc_markov_mat, urllc_resource_block, urllc_process_num, service_markov_mat, service_resources_block):
    betas = np.arange(1, 10, 0.00001)
    error_list = []
    max_z = 0
    for beta in betas:
        urllc_s = (math.log(
            urllc_markov_mat[0][1] * math.exp(beta * urllc_resource_block) + urllc_markov_mat[0][0])) / beta
        service_s = (math.log(
            service_markov_mat[0][1] * math.exp(-beta * service_resources_block) + service_markov_mat[0][0])) / -beta
        error = service_s - urllc_process_num * urllc_s
        error_list.append(error)
        if error > 0:
            max_z = beta
        else:
            break
    urllc_s = (math.log(
        urllc_markov_mat[0][1] * math.exp(max_z * urllc_resource_block) + urllc_markov_mat[0][0])) / max_z
    service_s = (math.log(
        service_markov_mat[0][1] * math.exp(-max_z * service_resources_block) + service_markov_mat[0][0])) / -max_z
    # print(urllc_process_num*urllc_s, service_s)
    return max_z
