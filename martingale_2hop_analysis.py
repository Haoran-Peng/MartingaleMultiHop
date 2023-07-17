import numpy as np
import math
import pandas as pd
from numpy import linalg as LA
import os


def analyze(urllc_markov_mat, urllc_resource_block, urllc_process_num, urllc_steady_vec,
            embb_markov_mat, embb_resource_block, embb_process_num, embb_steady_vec,
            service1_markov_mat, service2_markov_mat, service1_resources_block, service2_resource_block,
            service1_steady_vec, service2_steady_vec,
            edf_param, time_slot, case_name,scenario_name, eta):
    theta1, t_urllc1, eigv1_urllc, t_embb1, eigv1_embb, t1_service1, t1_service2, eigv1_service1, eigv1_service2 \
        = M1_param(urllc_markov_mat, urllc_resource_block, urllc_process_num, embb_markov_mat, embb_resource_block,
                   embb_process_num, service1_markov_mat, service2_markov_mat, service1_resources_block,
                   service2_resource_block, eta)
    init1, h1 = M1_init_condition(eigv1_urllc, urllc_steady_vec, eigv1_embb, embb_steady_vec, eigv1_service1,
                                  eigv1_service2, service1_steady_vec, service2_steady_vec)

    theta2, t_urllc2, eigv2_urllc, t2_service1, t2_service2, eigv2_service1, eigv2_service2 = \
        M2_param(urllc_markov_mat, urllc_resource_block, urllc_process_num, service1_markov_mat, service2_markov_mat,
                 service1_resources_block, service2_resource_block, eta)

    init2, h2 = M2_init_condition(eigv2_urllc, urllc_steady_vec, eigv2_service1, eigv2_service2, service1_steady_vec,
                                  service2_steady_vec)

    # print("2hop: :::",theta1, t1_service1, t1_service2, t_urllc1, t_embb1)
    # print("2hop: :::",theta2, t2_service1, t2_service2)

    FIFO(theta1, t_urllc1, t_embb1, t1_service1, t1_service2, init1, h1, time_slot, case_name,scenario_name, eta)
    SP_URLLC(theta2, t_urllc2, t2_service1, t2_service2, init2, h2, time_slot, case_name,scenario_name, eta)

    SP_eMBB(theta1, t_urllc1, t_embb1, t1_service1, t1_service2, init1, h1, time_slot, case_name,scenario_name, eta)

    EDF_URLLC(theta1, t_urllc1, t_embb1, t1_service1, t1_service2, init1, h1, theta2, t2_service1, t2_service2, init2,
              h2, edf_param, time_slot,
              case_name,scenario_name, eta)

    """ SP case 當urllc之服務比較高"""
    EDF_eMBB(theta1, t_urllc1, t_embb1, t1_service1, t1_service2, init1, h1, edf_param, time_slot, case_name,scenario_name, eta)

    Backlog(theta1, t_urllc1, t_embb1, t1_service1, t1_service2, init1, h1, case_name,scenario_name, eta)


def Backlog(theta, t_urllc, t_embb, t_service1, t_service2, init1, h1, case_name,scenario_name, eta):
    """ FIFO case 抓Ks中的比例"""

    delay = np.ones(4000)
    for i in range(0, 4000, 1):
        probability_EMBB = (init1 / h1) * (math.exp(-theta * i))
        delay[i] = probability_EMBB
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/BACKLOG.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish'+os.getcwd()+"/"+scenario_name+'/Martingale/2hop/' + case_name + '/BACKLOG.xlsx')
    writer.close()
    return None


def M1_init_condition(eigv_urllc, urllc_steady_vec, eigv_embb, embb_steady_vec, eigv_service1,
                      eigv_service_2, service1_steady_vec, service2_steady_vec):
    temp_urllc = eigv_urllc * urllc_steady_vec
    temp_embb = eigv_embb * embb_steady_vec
    temp_service1 = eigv_service1 * service1_steady_vec
    temp_service2 = eigv_service_2 * service2_steady_vec

    init_urllc = temp_urllc.sum()
    init_embb = temp_embb.sum()
    init_service1 = temp_service1.sum()
    init_service2 = temp_service2.sum()

    init1 = init_service1 * init_service2 * init_embb * init_urllc

    eigv_urllc.sort()
    eigv_embb.sort()
    eigv_service1.sort()

    h1 = eigv_urllc[0] * eigv_embb[0] * eigv_service1[0] * eigv_service_2[0]
    return init1, h1


def M2_init_condition(eigv_urllc, urllc_steady_vec, eigv_service1, eigv_service2, service1_steady_vec,
                      service2_steady_vec):
    temp_urllc = eigv_urllc * urllc_steady_vec
    temp_service1 = eigv_service1 * service1_steady_vec
    temp_service2 = eigv_service2 * service2_steady_vec

    init_urllc = temp_urllc.sum()
    init_service1 = temp_service1.sum()
    init_service2 = temp_service2.sum()

    init2 = init_service1 * init_service2 * init_urllc

    eigv_urllc.sort()
    eigv_service1.sort()
    eigv_service2.sort()

    h2 = eigv_urllc[0] * eigv_service1[0] * eigv_service2[0]
    return init2, h2


def M1_param(urllc_markov_mat, urllc_resource_block, urllc_process_num,
             embb_markov_mat, embb_resource_block, embb_process_num,
             service1_markov_mat, service2_markov_mat, service1_resources_block, service2_resources_block, eta):
    # print("\n==== Calculating the parameter of M1 ====\n")
    theta1 = 0
    t_urllc = 0
    t_embb = 0
    t_service1 = 0
    t_service2 = 0
    error1 = 1
    error2 = 1
    previous_error1 = -500
    previous_error2 = -500
    gap = 1
    while error1 > 0.00001 and error2 > 0.00001:
        theta1 += gap
        urllc_exp = np.array([1, math.exp(theta1 * urllc_resource_block)], np.float64)
        embb_exp = np.array([1, math.exp(theta1 * embb_resource_block)], np.float64)
        service1_exp = np.array([1, math.exp(theta1 * service1_resources_block * eta)], np.float64)
        service2_exp = np.array([1, math.exp(theta1 * service2_resources_block * (1 - eta))], np.float64)

        urllc_exp_trans = urllc_markov_mat * urllc_exp
        embb_exp_trans = embb_markov_mat * embb_exp
        service1_exp_trans = service1_markov_mat * service1_exp
        service2_exp_trans = service2_markov_mat * service2_exp

        eiga_urllc, eigv_urllc = LA.eig(urllc_exp_trans)
        eiga_embb, eigv_embb = LA.eig(embb_exp_trans)
        eiga_service1, eigv_service1 = LA.eig(service1_exp_trans)
        eiga_service2, eigv_service2 = LA.eig(service2_exp_trans)

        idx_eiga_urllc = abs(eiga_urllc).argmax(axis=0)
        idx_eiga_embb = abs(eiga_embb).argmax(axis=0)
        idx_eiga_service1 = abs(eiga_service1).argmax(axis=0)
        idx_eiga_service2 = abs(eiga_service2).argmax(axis=0)

        t_urllc = np.log(eiga_urllc[idx_eiga_urllc]) / theta1
        t_embb = np.log(eiga_embb[idx_eiga_embb]) / theta1
        t_service1 = np.log(eiga_service1[idx_eiga_service1]) / theta1 / eta
        t_service2 = np.log(eiga_service2[idx_eiga_service2]) / theta1 / (1 - eta)
        # print(t_service1, t_service2, t_urllc, t_embb)

        abs_eigv_urllc = abs(eigv_urllc[:, idx_eiga_urllc])
        abs_eigv_embb = abs(eigv_embb[:, idx_eiga_embb])
        abs_eigv_service1 = abs(eigv_service1[:, idx_eiga_service1])
        abs_eigv_service2 = abs(eigv_service2[:, idx_eiga_service2])

        error1 = t_service1 - urllc_process_num * t_urllc - embb_process_num * t_embb
        error2 = t_service2 - urllc_process_num * t_urllc - embb_process_num * t_embb
        # print(error1, error2, theta1)
        if error1 == previous_error1 or error2 == previous_error2:
            break
        else:
            previous_error1 = error1
            previous_error2 = error2

        if error1 < 0 or error2 < 0:
            error1 = 1
            error2 = 1
            theta1 = theta1 - gap
            gap = gap / 10

    return theta1, urllc_process_num * t_urllc, abs_eigv_urllc, embb_process_num * t_embb, abs_eigv_embb, t_service1, t_service2, abs_eigv_service1, abs_eigv_service2


def M2_param(urllc_markov_mat, urllc_resource_block, urllc_process_num,
             service1_markov_mat, service2_markov_mat, service1_resources_block, service2_resources_block, eta):
    # print("\n==== Calculating the parameter of M2 ====\n")
    theta2 = 0
    t_urllc = 0
    t_service1 = 0
    t_service2 = 0
    error1 = 1
    error2 = 1
    gap = 1
    while error1 > 0.00001 and error2 > 0.00001:
        theta2 += gap
        urllc_exp = np.array([1, math.exp(theta2 * urllc_resource_block)], np.float64)
        service_exp1 = np.array([1, math.exp(-theta2 * service1_resources_block * eta)], np.float64)
        service_exp2 = np.array([1, math.exp(-theta2 * service2_resources_block * (1 - eta))], np.float64)

        urllc_exp_trans = urllc_markov_mat * urllc_exp
        service1_exp_trans = service1_markov_mat * service_exp1
        service2_exp_trans = service2_markov_mat * service_exp2

        eiga_urllc, eigv_urllc = LA.eig(urllc_exp_trans)
        eiga_service1, eigv_service1 = LA.eig(service1_exp_trans)
        eiga_service2, eigv_service2 = LA.eig(service2_exp_trans)

        idx_eiga_urllc = abs(eiga_urllc).argmax(axis=0)
        idx_eiga_service1 = abs(eiga_service1).argmax(axis=0)
        idx_eiga_service2 = abs(eiga_service2).argmax(axis=0)

        t_urllc = np.log(eiga_urllc[idx_eiga_urllc]) / theta2
        t_service1 = np.log(eiga_service1[idx_eiga_service1]) / -theta2 / eta
        t_service2 = np.log(eiga_service2[idx_eiga_service2]) / -theta2 / (1 - eta)
        abs_eigv_urllc = abs(eigv_urllc[:, idx_eiga_urllc])
        abs_eigv_service1 = abs(eigv_service1[:, idx_eiga_service1])
        abs_eigv_service2 = abs(eigv_service2[:, idx_eiga_service2])

        error1 = t_service1 - urllc_process_num * t_urllc
        error2 = t_service2 - urllc_process_num * t_urllc

        if error1 < 0 or error2 < 0:
            error1 = 1
            error2 = 1
            theta2 = theta2 - gap
            gap = gap / 10

    # print("\n==== Finish the parameter of M2 ====\n")
    return theta2, urllc_process_num * t_urllc, abs_eigv_urllc, t_service1, t_service2, abs_eigv_service1, abs_eigv_service2


def FIFO(theta1, t_urllc1, t_embb1, t_service1, t_service2, init1, h1, time_slot, case_name,scenario_name, eta):
    # print(theta1, eta * t_service1 + (1 - eta) * t_service2)
    # print(init1 / h1)
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability_URLLC = (init1 / h1) * (math.exp(-theta1 * i * (eta * t_service1 + (1 - eta) * t_service2)))
        delay[i] = probability_URLLC

    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/FIFO_BOTH.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/FIFO_BOTH.xlsx')
    writer.close()
    return None


def SP_URLLC(theta2, t_urllc2, t_service1, t_service2, init2, h2, time_slot, case_name,scenario_name, eta):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = (init2 / h2) * (math.exp(-theta2 * i * (eta * t_service1 + (1 - eta) * t_service2)))
        delay[i] = probability

    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/SP_URLLC.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/SP_URLLC.xlsx')
    writer.close()
    return None


def SP_eMBB(theta1, t_urllc1, t_embb1, t_service1, t_service2, init1, h1, time_slot, case_name,scenario_name, eta):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = (init1 / h1) * (math.exp(-theta1 * i * ((eta * t_service1 + (1 - eta) * t_service2) - t_urllc1)))
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/SP_eMBB.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/SP_eMBB.xlsx')
    writer.close()
    return None


def EDF_URLLC(theta1, t_urllc1, t_embb1, t1_service1, t1_service2, init1, h1, theta2, t2_service1, t2_service2, init2,
              h2, edf_param, time_slot,
              case_name,scenario_name, eta):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        probability = (init1 / h1) * (
            math.exp(-theta1 * (i * (eta * t1_service1 + (1 - eta) * t1_service2) + edf_param * t_embb1))) + (
                                  init1 / h1) * (
                          math.exp(-theta2 * i * (eta * t2_service1 + (1 - eta) * t2_service2)))
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/EDF_URLLC.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/EDF_URLLC.xlsx')
    writer.close()
    return None


def EDF_eMBB(theta1, t_urllc1, t_embb1, t_service1, t_service2, init1, h1, edf_param, time_slot, case_name,scenario_name, eta):
    delay = np.ones(4000)
    delay_label = []
    for i in range(4000):
        delay_label.append(i * time_slot)
    for i in range(0, 4000, 1):
        if i >= edf_param:
            probability = (init1 / h1) * (
                math.exp(-theta1 * (i * (eta * t_service1 + (1 - eta) * t_service2) - edf_param * t_urllc1)))
        else:
            probability = (init1 / h1) * (
                math.exp(-theta1 * (i * ((eta * t_service1 + (1 - eta) * t_service2) - t_urllc1))))
        delay[i] = probability
    df = pd.DataFrame(delay).T
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/EDF_eMBB.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    print('finish' + os.getcwd() + "/" + scenario_name + '/Martingale/2hop/' + case_name + '/EDF_eMBB.xlsx')
    writer.close()
    return None
