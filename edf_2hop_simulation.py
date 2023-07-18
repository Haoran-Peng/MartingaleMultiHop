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
               service_markov_mat1, service_resource_block1, service_markov_mat2, service_resource_block2, edf_param2,
               slot_num, runs, case_name,scenario_name):
    urllc_arrival_network = np.zeros([runs, slot_num + 1])
    embb_arrival_network = np.zeros([runs, slot_num + 1])
    urllc_service_network1 = np.zeros([runs, slot_num + 1])
    embb_service_network1 = np.zeros([runs, slot_num + 1])
    urllc_service_network2 = np.zeros([runs, slot_num + 1])
    embb_service_network2 = np.zeros([runs, slot_num + 1])
    non_service_prob1 = service_markov_mat1[0][0] * 100000
    non_service_prob2 = service_markov_mat2[0][0] * 100000

    runs_blank1 = []
    runs_blank2 = []
    runs_blank3 = []

    for run in range(runs):
        urllc_total_arrival1 = 0
        embb_total_arrival1 = 0
        urllc_total_service1 = 0
        embb_total_service1 = 0
        urllc_total_service2 = 0
        embb_total_service2 = 0
        urllc_backlog1 = 0
        embb_backlog1 = 0
        urllc_backlog2 = 0
        embb_backlog2 = 0

        urllc_workload1 = []
        urllc_time1 = []
        embb_workload1 = []
        embb_time1 = []
        urllc_idx1 = 0
        embb_idx1 = 0
        urllc_idx2 = 0
        embb_idx2 = 0
        blank1 = 0
        blank2 = 0
        blank3 = 0
        flag1 = 0
        flag2 = 0
        left1 = urllc_resource_block
        left2 = embb_resource_block

        for time in range(1, slot_num + 1, 1):
            service1 = get_service(service_resource_block1, non_service_prob1)
            service2 = get_service(service_resource_block2, non_service_prob2)

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

            if time == 1:
                urllc_backlog2 += urllc_service_network1[run][time - 1]
                embb_backlog2 += embb_service_network1[run][time - 1]
            if time > 1:
                urllc_backlog2 += int(urllc_service_network1[run][time - 1] - urllc_service_network1[run][time - 2])
                embb_backlog2 += int(embb_service_network1[run][time - 1] - embb_service_network1[run][time - 2])

            while service1 > 0 and (urllc_backlog1 > 0 or embb_backlog1 > 0):
                if urllc_backlog1 > 0 and embb_backlog1 > 0:
                    tc_current_time = urllc_time1[urllc_idx1]
                    eb_current_time = embb_time1[embb_idx1]
                    if tc_current_time == eb_current_time + edf_param2:
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
                                    embb_backlog1 = int(embb_backlog1-work)
                                    # embb_total_service1 = int(embb_total_service1+embb_resource_block)
                                    embb_total_service1 += work
                                    service1 = int(service1 - work)
                                    embb_idx1 += 1
                                    flag1 = 0
                                else:
                                    embb_backlog1 = int(embb_backlog1-service1)
                                    embb_total_service1 += service1
                                    embb_workload1[embb_idx1] = int(embb_workload1[embb_idx1]-service1)
                                    service1 = 0
                        else:
                            work = embb_workload1[embb_idx1]
                            if work <= service1:
                                embb_backlog1 -= work
                                # embb_total_service1 += embb_resource_block
                                embb_total_service1 += work
                                service1 = round(service1 - work)
                                embb_idx1 += 1
                                flag1 = 0
                            else:
                                embb_backlog1 -= service1
                                embb_total_service1 += service1
                                embb_workload1[embb_idx1] -= service1
                                service1 = 0
                    elif tc_current_time < eb_current_time + edf_param2:
                        work = int(urllc_workload1[urllc_idx1])
                        urllc_backlog1 = int(urllc_backlog1-work)
                        urllc_total_service1 = int(urllc_total_service1+work)
                        service1 = round(service1 - work)
                        urllc_idx1 += 1
                    else:
                        work = int(embb_workload1[embb_idx1])
                        if work <= service1:
                            embb_backlog1 -= work
                            embb_total_service1 += work
                            # embb_total_service1 += embb_resource_block
                            service1 = round(service1 - work)
                            embb_idx1 += 1

                        else:
                            embb_backlog1 -= service1
                            embb_total_service1 += service1
                            embb_workload1[embb_idx1] -= service1
                            service1 = 0

                elif urllc_backlog1 > 0:
                    work = urllc_workload1[urllc_idx1]
                    if work <= service1:
                        urllc_backlog1 -= work
                        urllc_total_service1 += work
                        service1 = round(service1 - work)
                        urllc_idx1 += 1
                    else:
                        urllc_backlog1 -= service1
                        urllc_total_service1 += service1
                        urllc_workload1[urllc_idx1] -= service1
                        service1 = 0
                else:
                    work = int(embb_workload1[embb_idx1])
                    if work <= service1:
                        embb_backlog1 = int(embb_backlog1-work)
                        # embb_total_service1 = int(embb_total_service1+embb_resource_block)
                        embb_total_service1 += work
                        service1 = int(service1 - work)
                        embb_idx1 += 1

                    else:
                        embb_backlog1 -= service1
                        embb_total_service1 += service1
                        embb_workload1[embb_idx1] -= service1
                        service1 = 0
            urllc_service_network1[run][time] = int(urllc_total_service1)
            embb_service_network1[run][time] = int(embb_total_service1)

            while service2 > 0 and (urllc_backlog2 > 0 or embb_backlog2 > 0):
                if urllc_backlog2 > 0 and embb_backlog2 > 0:
                    tc_current_time = urllc_time1[urllc_idx2]
                    eb_current_time = embb_time1[embb_idx2]
                    if tc_current_time == eb_current_time + edf_param2:
                        if flag2 == 0:
                            flag2 = 1
                            turn2 = random.randint(0, 1)
                            if turn2 == 0:
                                work = left1
                                urllc_backlog2 -= work
                                urllc_total_service2 = int(urllc_total_service2+work)
                                service2 = int(service2 - work)
                                urllc_idx2 += 1
                                flag2 = 0
                                left1 = urllc_resource_block

                            else:
                                work = left2
                                if work <= service2:
                                    embb_backlog2 -= work
                                    embb_total_service2 += work
                                    # embb_total_service2 += embb_resource_block
                                    service2 = int(service2 - work)
                                    embb_idx2 += 1
                                    flag2 = 0
                                    left2 = embb_resource_block
                                else:
                                    embb_backlog2 = int(embb_backlog2-service2)
                                    embb_total_service2 += service2
                                    left2 = int(left2 - service2)
                                    service2 = 0
                        else:
                            work = int(left2)
                            if work <= service2:
                                embb_backlog2 -= work
                                # embb_total_service2 += embb_resource_block
                                embb_total_service2 += work
                                service2 = int(service2 - work)
                                embb_idx2 += 1
                                flag2 = 0
                                left2 = embb_resource_block
                            else:
                                embb_backlog2 = int(embb_backlog2-service2)
                                embb_total_service2 += service2
                                left2 = int(left2 - service2)
                                service2 = 0
                    elif tc_current_time < eb_current_time + edf_param2:
                        work = left1
                        urllc_backlog2 = round(urllc_backlog2-work)
                        urllc_total_service2 = round(urllc_total_service2+work)
                        service2 = round(service2 - work)
                        urllc_idx2 += 1
                        left1 = urllc_resource_block
                    else:
                        work = left2
                        if work <= service2:
                            embb_backlog2 = round(embb_backlog2-work)
                            embb_total_service2 += work
                            # embb_total_service2 += embb_resource_block
                            service2 = round(service2 - work)
                            embb_idx2 += 1
                            left2 = embb_resource_block
                        else:
                            embb_backlog2 -= service2
                            embb_total_service2 += service2
                            left2 -= service2
                            service2 = 0

                elif urllc_backlog2 > 0:
                    work = left1
                    urllc_backlog2 -= work
                    urllc_total_service2 = int(urllc_total_service2+work)
                    service2 = int(service2 - work)
                    urllc_idx2 += 1
                    left1 = urllc_resource_block
                else:
                    work = left2
                    if work <= service2:
                        embb_backlog2 -= work
                        # embb_total_service2 = int(embb_total_service2+embb_resource_block)
                        embb_total_service2 += work
                        service2 = int(service2 - work)
                        embb_idx2 += 1
                        left2 = embb_resource_block
                    else:
                        embb_backlog2 -= service2
                        embb_total_service2 += service2
                        left2 = int(left2-service2)
                        service2 = 0

            if service1 == service_resource_block1:
                blank1 += 1

            if service2 == service_resource_block2:
                blank2 += 1

            if service1 == service_resource_block1 and service2 == service_resource_block2:
                blank3 += 1

            urllc_service_network2[run][time] = urllc_total_service2
            embb_service_network2[run][time] = embb_total_service2

        runs_blank1.append(blank1)
        runs_blank2.append(blank2)
        runs_blank3.append(blank3)

    # write_data(urllc_arrival_network, urllc_service_network1, slot_num, runs, runs_blank1, case_name, 'EDF_URLLC',
    #            "1hop")
    # write_data1(embb_arrival_network, embb_service_network1, slot_num, runs, runs_blank1, case_name, 'EDF_eMBB', "1hop")
    write_data2(urllc_arrival_network, urllc_service_network1, urllc_service_network2, slot_num, runs, runs_blank1, runs_blank2, runs_blank3, case_name,scenario_name, 'EDF_URLLC',
               "2hop")
    write_data2(embb_arrival_network, embb_service_network1, embb_service_network2, slot_num, runs, runs_blank1, runs_blank2, runs_blank3, case_name,scenario_name, 'EDF_eMBB', "2hop")
    return urllc_arrival_network, urllc_service_network1, embb_arrival_network, embb_service_network1


def write_data2(arrival_network, service_network1, service_network2, slot_num, runs, blank1, blank2, blank3, case_name,scenario_name, case_d,
                hop):
    delay_size = 4000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (delay_size + 1)
        delay_ccdf = [0] * delay_size
        prev1 = 0
        prev_2 = 0

        for time in range(1, slot_num + 1, 1):
            service_amount = service_network2[run][time]
            while time + 1 > prev1 and prev1 < 100001:
                if arrival_network[run][prev1] > service_amount:
                    break
                else:
                    prev1 += 1
            delay = time - prev1 + 1
            if delay > 4000:
                delay_list[3999] += 1
            else:
                delay_list[delay] += 1
        # for time in range(1, slot_num + 1, 1):
        #     service_amount2 = service_network1[run][time]
        #
        #     while time + 1 > prev_2 and prev_2 < 100001:
        #         if arrival_network[run][prev_2] > service_amount2:
        #             break
        #         else:
        #             prev_2 += 1
        #     delay2 = time - prev_2 + 1
        #     if delay2 > 4000:
        #         delay_list[3999] += 1
        #     else:
        #         delay_list[delay2] += 1
        #
        total = 0
        delay_list[0] -= (blank3[run])

        # delay_list[0] -= (blank3[run]+blank1[run])
        for i in range(delay_size + 1):
            total += delay_list[i]
        drag = total
        for i in range(delay_size):
            delay_ccdf[i] = drag / total
            drag -= delay_list[i]
        run_data.append(delay_ccdf)

    df = pd.DataFrame(run_data)
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name+"/Simulation/" + hop + '/' + case_name + "/" + case_d + '.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return None

