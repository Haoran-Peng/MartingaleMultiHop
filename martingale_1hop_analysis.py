import numpy as np
import math
import pandas as pd
from numpy import linalg as LA
import os

def analyze(urllc_markov_mat, urllc_resource_block, urllc_process_num, urllc_steady_vec,
            embb_markov_mat, embb_resource_block, embb_process_num, embb_steady_vec,
            service_markov_mat, service_resources_block, service_steady_vec, edf_param, time_slot, case_name, scenario_name):
    theta1, t_urllc1, eigv1_urllc, t_embb1, eigv1_embb, t_service1, eigv1_service \
        = M1_param(urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block,
                   embb_process_num, service_markov_mat, service_resources_block)
    init1, h1 = M1_init_condition(eigv1_urllc, urllc_steady_vec, eigv1_embb, embb_steady_vec, eigv1_service,
                                  service_steady_vec)
    # print("1hop:::", theta1, t_service1, t_urllc1, t_embb1)
    theta2, t_urllc2, eigv2_urllc, t_service2, eigv2_service = M2_param(urllc_markov_mat, urllc_resource_block,
                                                                        urllc_process_num, service_markov_mat,
                                                                        service_resources_block)
    init2, h2 = M2_init_condition(eigv2_urllc, urllc_steady_vec, eigv2_service, service_steady_vec)

    FIFO(theta1, t_urllc1, t_embb1, t_service1, init1, h1, time_slot, case_name,scenario_name)

    SP_URLLC(theta2, t_urllc2, t_service2, init2, h2, time_slot, case_name,scenario_name)

    SP_eMBB(theta1, t_urllc1, t_embb1, t_service1, init1, h1, time_slot, case_name,scenario_name)

    EDF_URLLC(theta1, t_urllc1, t_embb1, t_service1, init1, h1, theta2, t_service2, init2, h2, edf_param, time_slot,
              case_name,scenario_name)
    """ SP case 當urllc之服務比較高"""
    EDF_eMBB(theta1, t_urllc1, t_embb1, t_service1, init1, h1, edf_param, time_slot, case_name,scenario_name)

    Backlog(theta1, t_urllc1, t_embb1, t_service1, init1, h1, case_name,scenario_name)


def Backlog(theta, t_urllc, t_embb, t_service, init1, h1, case_name, scenario_name):
    """ FIFO case 抓Ks中的比例"""
    delay = np.ones(4000)

    for i in range(0, 4000, 1):
        probability_EMBB = (init1 / h1) * (math.exp(-theta * i))
        delay[i] = probability_EMBB
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd()+"/"+scenario_name + '/Martingale/1hop/' + case_name + '/BACKLOG.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/BACKLOG.xlsx')
    writer.close()
    return None


def M1_init_condition(eigv_urllc, urllc_steady_vec, eigv_embb, embb_steady_vec, eigv_service, service_steady_vec):
    temp_urllc = eigv_urllc * urllc_steady_vec
    temp_embb = eigv_embb * embb_steady_vec
    temp_service = eigv_service * service_steady_vec

    init_urllc = temp_urllc.sum()
    init_embb = temp_embb.sum()
    init_service = temp_service.sum()
    init1 = init_service * init_embb * init_urllc

    eigv_urllc.sort()
    eigv_embb.sort()
    eigv_service.sort()

    h1 = eigv_urllc[0] * eigv_embb[0] * eigv_service[0]
    return init1, h1


def M2_init_condition(eigv_urllc, urllc_steady_vec, eigv_service, service_steady_vec):
    temp_urllc = eigv_urllc * urllc_steady_vec
    temp_service = eigv_service * service_steady_vec

    init_urllc = temp_urllc.sum()
    init_service = temp_service.sum()

    init2 = init_service * init_urllc

    eigv_urllc.sort()
    eigv_service.sort()

    h2 = eigv_urllc[0] * eigv_service[0]
    return init2, h2


def M1_param(urllc_markov_mat, urllc_resource_block, urllc_process_num,
             embb_markov_mat, embb_resource_block, embb_process_num,
             service_markov_mat, service_resources_block):
    # print("\n==== Calculating the parameter of M1 ====\n")
    theta1 = 0
    t_urllc = 0
    t_embb = 0
    t_service = 0
    error = 1
    gap = 1
    while error > 0.00001:
        theta1 += gap
        urllc_exp = np.array([1, math.exp(theta1 * urllc_resource_block)], np.float64)
        embb_exp = np.array([1, math.exp(theta1 * embb_resource_block)], np.float64)
        service_exp = np.array([1, math.exp(theta1 * service_resources_block)], np.float64)
        urllc_exp_trans = urllc_markov_mat * urllc_exp
        embb_exp_trans = embb_markov_mat * embb_exp
        service_exp_trans = service_markov_mat * service_exp
        # print('0',urllc_markov_mat ,"\n", embb_markov_mat, "\n", service_markov_mat, "\n")

        # print('1',urllc_exp_trans, "\n", embb_exp_trans, "\n", service_exp_trans, "\n")
        eiga_urllc, eigv_urllc = LA.eig(urllc_exp_trans)
        eiga_embb, eigv_embb = LA.eig(embb_exp_trans)
        eiga_service, eigv_service = LA.eig(service_exp_trans)
        # print('2',eiga_urllc, "\n", eiga_embb, "\n", eiga_service, "\n")
        # print('3',eigv_urllc, "\n", eigv_embb, "\n", eigv_service, "\n")

        idx_eiga_urllc = abs(eiga_urllc).argmax(axis=0)
        idx_eiga_embb = abs(eiga_embb).argmax(axis=0)
        idx_eiga_service = abs(eiga_service).argmax(axis=0)
        # print('5',idx_eiga_urllc ,"\n", idx_eiga_embb, "\n", idx_eiga_service,"\n")

        t_urllc = np.log(eiga_urllc[idx_eiga_urllc]) / theta1
        t_embb = np.log(eiga_embb[idx_eiga_embb]) / theta1
        t_service = np.log(eiga_service[idx_eiga_service]) / theta1
        # print(t_urllc, t_embb, t_service)
        abs_eigv_urllc = abs(eigv_urllc[:, idx_eiga_urllc])
        abs_eigv_embb = abs(eigv_embb[:, idx_eiga_embb])
        abs_eigv_service = abs(eigv_service[:, idx_eiga_service])
        error = t_service - urllc_process_num * t_urllc - embb_process_num * t_embb
        # print(error, theta1)
        if error < 0:
            error = 1
            theta1 = theta1 - gap
            gap = gap / 10

    # print("\n==== Finish the parameter of M1 ====\n")
    return theta1, urllc_process_num * t_urllc, abs_eigv_urllc, embb_process_num * t_embb, abs_eigv_embb, t_service, abs_eigv_service


def M2_param(urllc_markov_mat, urllc_resource_block, urllc_process_num,
             service_markov_mat, service_resources_block):
    # print("\n==== Calculating the parameter of M2 ====\n")
    theta2 = 0
    t_urllc = 0
    t_service = 0
    error = 1
    gap = 1
    while error > 0.00001:
        theta2 += gap
        urllc_exp = np.array([1, math.exp(theta2 * urllc_resource_block)], np.float64)
        service_exp = np.array([1, math.exp(-theta2 * service_resources_block)], np.float64)

        urllc_exp_trans = urllc_markov_mat * urllc_exp
        service_exp_trans = service_markov_mat * service_exp

        eiga_urllc, eigv_urllc = LA.eig(urllc_exp_trans)
        eiga_service, eigv_service = LA.eig(service_exp_trans)

        idx_eiga_urllc = abs(eiga_urllc).argmax(axis=0)
        idx_eiga_service = abs(eiga_service).argmax(axis=0)

        t_urllc = np.log(eiga_urllc[idx_eiga_urllc]) / theta2
        t_service = np.log(eiga_service[idx_eiga_service]) / (-theta2)

        abs_eigv_urllc = abs(eigv_urllc[:, idx_eiga_urllc])
        abs_eigv_service = abs(eigv_service[:, idx_eiga_service])

        error = t_service - urllc_process_num * t_urllc
        if error < 0:
            error = 1
            theta2 = theta2 - gap
            gap = gap / 10

    # print("\n==== Finish the parameter of M2 ====\n")
    return theta2, urllc_process_num * t_urllc, abs_eigv_urllc, t_service, abs_eigv_service


def FIFO(theta1, t_urllc1, t_embb1, t_service1, init1, h1, time_slot, case_name, scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability_URLLC = (init1 / h1) * (math.exp(-theta1 * i * t_service1))
        delay[i] = probability_URLLC

    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/FIFO_BOTH.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/FIFO_BOTH.xlsx')
    writer.close()
    return None


def SP_URLLC(theta2, t_urllc2, t_service2, init2, h2, time_slot, case_name, scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = (init2 / h2) * (math.exp(-theta2 * i * t_service2))
        delay[i] = probability

    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/SP_URLLC.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/SP_URLLC.xlsx')
    writer.close()
    return None


def SP_eMBB(theta1, t_urllc1, t_embb1, t_service1, init1, h1, time_slot, case_name,scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = (init1 / h1) * (math.exp(-theta1 * i * (t_service1 - t_urllc1)))
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name+'/Martingale/1hop/' + case_name + '/SP_eMBB.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/SP_eMBB.xlsx')
    writer.close()
    return None


def EDF_URLLC(theta1, t_urllc1, t_embb1, t_service1, init1, h1, theta2, t_service2, init2, h2, edf_param, time_slot,
              case_name, scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = (init1 / h1) * (math.exp(-theta1 * (i * t_service1 + edf_param * t_embb1))) + (init1 / h1) * (
            math.exp(-theta2 * i * t_service2))
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name+'/Martingale/1hop/' + case_name + '/EDF_URLLC.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/EDF_URLLC.xlsx')
    writer.close()
    return None


def EDF_eMBB(theta1, t_urllc1, t_embb1, t_service1, init1, h1, edf_param, time_slot, case_name, scenario_name):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        if i >= edf_param:
            probability = (init1 / h1) * (math.exp(-theta1 * (i * t_service1 - edf_param * t_urllc1)))
        else:
            probability = (init1 / h1) * (math.exp(-theta1 * (i * (t_service1 - t_urllc1))))
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/EDF_eMBB.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/1hop/' + case_name + '/EDF_eMBB.xlsx')
    writer.close()
    return None
