import numpy as np
import random
import pandas as pd
import os


def get_service(service_resource_block, prob):
    ss = 0
    for i in range(service_resource_block):
        service_prob = random.randint(1, 100000)
        if prob < service_prob:
            ss += 1
    return ss


def simulation(urllc_arrival_process, embb_arrival_process, urllc_resource_block, embb_resource_block,
               service_markov_mat1, service_resource_block1, service_markov_mat2, service_resource_block2, edf_param,
               slot_num, runs, case_name, scenario_name):
    urllc_arrival_network = np.zeros([runs, slot_num + 1])
    embb_arrival_network = np.zeros([runs, slot_num + 1])
    urllc_service_network1 = np.zeros([runs, slot_num + 1])
    embb_service_network1 = np.zeros([runs, slot_num + 1])
    non_service_prob1 = service_markov_mat1[0][0] * 100000
    runs_blank1 = []
    for run in range(runs):
        urllc_total_arrival1 = 0
        embb_total_arrival1 = 0
        urllc_total_service1 = 0
        embb_total_service1 = 0
        urllc_backlog1 = 0
        embb_backlog1 = 0
        urllc_workload1 = []
        urllc_time1 = []
        embb_workload1 = []
        embb_time1 = []
        urllc_idx1 = 0
        embb_idx1 = 0
        blank1 = 0
        flag1 = 0

        for time in range(1, slot_num + 1, 1):
            service1 = get_service(service_resource_block1, non_service_prob1)

            urllc_count_per_time = urllc_arrival_process[run][time]
            embb_count_per_time = embb_arrival_process[run][time]
            urllc_total_arrival1 += int(urllc_count_per_time * urllc_resource_block)
            embb_total_arrival1 += int(embb_count_per_time * embb_resource_block)

            urllc_arrival_network[run][time] = urllc_total_arrival1
            embb_arrival_network[run][time] = embb_total_arrival1

            urllc_backlog1 += int(urllc_count_per_time * urllc_resource_block)
            embb_backlog1 += int(embb_count_per_time * embb_resource_block)

            for i in range(int(urllc_count_per_time)):
                urllc_workload1.append(urllc_resource_block)
                urllc_time1.append(time)
            for i in range(int(embb_count_per_time)):
                embb_workload1.append(embb_resource_block)
                embb_time1.append(time)

            while service1 > 0 and (urllc_backlog1 > 0 or embb_backlog1 > 0):
                if urllc_backlog1 > 0 and embb_backlog1 > 0:
                    tc_current_time = urllc_time1[urllc_idx1]
                    eb_current_time = embb_time1[embb_idx1]
                    if tc_current_time == eb_current_time + edf_param:
                        if flag1 == 0:
                            flag1 = 1
                            turn1 = random.randint(0, 1)
                            if turn1 == 0:
                                work = int(urllc_workload1[urllc_idx1])
                                urllc_backlog1 = int(urllc_backlog1-work)
                                urllc_total_service1 = int(urllc_total_service1+work)
                                service1 = int(service1 - work)
                                urllc_idx1 += 1
                                flag1 = 0

                            else:
                                work = int(embb_workload1[embb_idx1])
                                if work <= service1:
                                    embb_backlog1 -= work
                                    embb_total_service1 += embb_resource_block
                                    service1 = int(service1 - work)
                                    embb_idx1 += 1
                                    flag1 = 0
                                else:
                                    embb_backlog1 = int(embb_backlog1-service1)
                                    embb_workload1[embb_idx1] = int(embb_workload1[embb_idx1] - service1)
                                    service1 = 0
                        else:
                            work = int(embb_workload1[embb_idx1])
                            if work <= service1:
                                embb_backlog1 -= work
                                embb_total_service1 += embb_resource_block
                                service1 = round(service1 - work)
                                embb_idx1 += 1
                                flag1 = 0
                            else:
                                embb_backlog1 -= service1
                                embb_workload1[embb_idx1] -= service1
                                service1 = 0
                    elif tc_current_time < eb_current_time + edf_param:
                        work = urllc_workload1[urllc_idx1]
                        urllc_backlog1 = int(urllc_backlog1-work)
                        urllc_total_service1 += work
                        service1 = int(service1 - work)
                        urllc_idx1 += 1
                    else:
                        work = int(embb_workload1[embb_idx1])
                        if work <= service1:
                            embb_backlog1 = int(embb_backlog1-work)
                            embb_total_service1 += embb_resource_block
                            service1 = int(service1 - work)
                            embb_idx1 += 1

                        else:
                            embb_backlog1 -= service1
                            embb_workload1[embb_idx1] -= service1
                            service1 = 0

                elif urllc_backlog1 > 0:
                    work = int(urllc_workload1[urllc_idx1])
                    urllc_backlog1 = int(urllc_backlog1-work)
                    urllc_total_service1 = int(urllc_total_service1+work)
                    service1 = int(service1 - work)
                    urllc_idx1 += 1
                else:
                    work = int(embb_workload1[embb_idx1])
                    if work <= service1:
                        embb_backlog1 = int(embb_backlog1-work)
                        embb_total_service1 = int(embb_total_service1+embb_resource_block)
                        service1 = round(service1 - work)
                        embb_idx1 += 1

                    else:
                        embb_backlog1 = int(embb_backlog1-service1)
                        embb_workload1[embb_idx1] -= service1
                        service1 = 0
            urllc_service_network1[run][time] = int(urllc_total_service1)
            embb_service_network1[run][time] = int(embb_total_service1)

            if service1 == service_resource_block1:
                blank1 += 1

        runs_blank1.append(blank1)

    write_data(urllc_arrival_network, urllc_service_network1, slot_num, runs, runs_blank1, case_name,scenario_name, 'EDF_URLLC',
               "1hop")
    write_data1(embb_arrival_network, embb_service_network1, slot_num, runs, runs_blank1, case_name,scenario_name, 'EDF_eMBB', "1hop")
    return urllc_arrival_network, urllc_service_network1, embb_arrival_network, embb_service_network1


def write_data(arrival_network, service_network, slot_num, runs, blank, case_name,scenario_name, case_d, hop):
    delay_size = 4000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (delay_size + 1)
        delay_ccdf = [0] * delay_size
        for time in range(1, slot_num + 1, 1):
            delay = 0
            service_amount = service_network[run][time]
            while time - delay >= 0:
                if arrival_network[run][time - delay] <= service_amount:
                    if delay >= 4000:
                        delay_list[4000] += 1
                        break
                    else:
                        delay_list[delay] += 1
                        break
                else:
                    delay += 1
        total = 0
        delay_list[0] -= blank[run]
        for i in range(delay_size):
            total += delay_list[i]
        drag = total

        for i in range(delay_size):
            delay_ccdf[i] = drag / total
            drag -= delay_list[i]
        run_data.append(delay_ccdf)

    df = pd.DataFrame(run_data)
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + "/Simulation/" + hop + '/' + case_name + "/" + case_d + '.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return None


def write_data1(arrival_network, service_network, slot_num, runs, blank, case_name,scenario_name, case_d, hop):
    delay_size = 4000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (delay_size + 1)
        delay_ccdf = [0] * delay_size
        prev = 0
        for time in range(1, slot_num + 1, 1):
            service_amount = service_network[run][time]
            while time+1 > prev and prev < 100001:
                if arrival_network[run][prev] > service_amount:
                    break
                else:
                    prev += 1
            delay = time - prev + 1
            if delay > 4000:
                delay_list[3999] += 1
            else:
                delay_list[delay] += 1

        total = 0
        delay_list[0] -= blank[run]
        for i in range(delay_size+1):
            total += delay_list[i]
        drag = total
        for i in range(delay_size):
            delay_ccdf[i] = drag / total
            drag -= delay_list[i]
        run_data.append(delay_ccdf)

    df = pd.DataFrame(run_data)
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name + "/Simulation/" + hop + '/' + case_name + "/" + case_d + '.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return None
