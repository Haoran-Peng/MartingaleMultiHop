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
               service_markov_mat1, service_resource_block1, service_markov_mat2, service_resource_block2, slot_num,
               runs, case_name, scenario_name):
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
    backlog_runs_network1 = []
    backlog_runs_network2 = []
    for run in range(runs):
        urllc_total_arrival = 0
        embb_total_arrival = 0
        urllc_total_service1 = 0
        embb_total_service1 = 0
        urllc_total_service2 = 0
        embb_total_service2 = 0
        urllc_backlog1 = 0
        embb_backlog1 = 0
        urllc_backlog2 = 0
        embb_backlog2 = 0
        backlog_network2 = []
        backlog_network1 = []
        queue_type = []
        queue_idx1 = 0
        queue_idx2 = 0
        blank1 = 0
        blank2 = 0
        x = 0
        left12 = embb_resource_block
        left22 = embb_resource_block
        for time in range(1, slot_num + 1, 1):
            service1 = get_service(service_resource_block1, non_service_prob1)
            service2 = get_service(service_resource_block2, non_service_prob2)

            urllc_count_per_time = urllc_arrival_process[run][time]
            embb_count_per_time = embb_arrival_process[run][time]

            urllc_total_arrival += int(urllc_count_per_time * urllc_resource_block)
            embb_total_arrival += int(embb_count_per_time * embb_resource_block)
            urllc_arrival_network[run][time] = urllc_total_arrival
            embb_arrival_network[run][time] = embb_total_arrival
            urllc_backlog1 += int(urllc_count_per_time * urllc_resource_block)
            embb_backlog1 += int(embb_count_per_time * embb_resource_block)

            if time == 1:
                urllc_backlog2 += urllc_service_network1[run][time - 1]
                embb_backlog2 += embb_service_network1[run][time - 1]
            if time > 1:
                urllc_backlog2 += int(urllc_service_network1[run][time - 1] - urllc_service_network1[run][time - 2])
                embb_backlog2 += int(embb_service_network1[run][time - 1] - embb_service_network1[run][time - 2])

            for idx in range(int(urllc_count_per_time + embb_count_per_time)):
                if urllc_count_per_time != 0 and embb_count_per_time != 0:
                    fair = random.randint(0, 1)
                    if fair == 0:
                        queue_type.append(0)
                        urllc_count_per_time -= 1
                    else:
                        queue_type.append(1)
                        embb_count_per_time -= 1
                elif urllc_count_per_time != 0:
                    queue_type.append(0)
                    urllc_count_per_time -= 1
                else:
                    queue_type.append(1)
                    embb_count_per_time -= 1

            while service1 > 0 and (int(urllc_backlog1) > 0 or int(embb_backlog1) > 0):
                if queue_type[queue_idx1] == 0:
                    urllc_backlog1 = int(urllc_backlog1 - 1)
                    urllc_total_service1 = int(urllc_total_service1 + 1)
                    service1 = int(service1 - 1)
                    queue_idx1 += 1
                else:
                    work = left12
                    if work <= service1:
                        embb_backlog1 = int(embb_backlog1 - work)
                        embb_total_service1 += work
                        service1 = int(service1 - work)
                        queue_idx1 += 1
                        left12 = embb_resource_block
                    else:
                        embb_backlog1 = int(embb_backlog1 - service1)
                        embb_total_service1 += service1
                        left12 = int(left12 - service1)
                        service1 = 0
            urllc_service_network1[run][time] = urllc_total_service1
            embb_service_network1[run][time] = embb_total_service1

            while service2 > 0 and (urllc_backlog2 > 0 or embb_backlog2 > 0):
                if queue_type[queue_idx2] == 0:
                    urllc_backlog2 = int(urllc_backlog2 - 1)
                    urllc_total_service2 = int(urllc_total_service2 + 1)
                    service2 = int(service2 - 1)
                    queue_idx2 += 1
                else:
                    work = left22
                    if work <= service2:
                        embb_backlog2 -= work
                        # embb_total_service2 = int(embb_total_service2+embb_resource_block)
                        embb_total_service2 = int(embb_total_service2 + work)
                        service2 = int(service2 - work)
                        queue_idx2 += 1
                        left22 = embb_resource_block
                    else:
                        embb_backlog2 = int(embb_backlog2 - service2)
                        embb_total_service2 += service2
                        left22 = int(left22 - service2)
                        service2 = 0

            if service1 == service_resource_block1:
                blank1 += 1
            if service1 == service_resource_block1 and service2 == service_resource_block2:
                blank2 += 1
            if service1 != service_resource_block1:
                backlog_network1.append(urllc_backlog1 + embb_backlog1)
            if service1 != service_resource_block1 or service2 != service_resource_block2:
                backlog_network2.append(int(urllc_backlog2 + embb_backlog2 + urllc_backlog1 + embb_backlog1))

            urllc_service_network2[run][time] = urllc_total_service2
            embb_service_network2[run][time] = embb_total_service2
        runs_blank1.append(blank1)
        runs_blank2.append(blank2)
        backlog_runs_network1.append(backlog_network1)
        backlog_runs_network2.append(backlog_network2)

    write_data(urllc_arrival_network, urllc_service_network1, slot_num, runs, runs_blank1, case_name, scenario_name,
               'FIFO_URLLC', "1hop")
    write_data1(embb_arrival_network, embb_service_network1, slot_num, runs, runs_blank1, case_name, scenario_name,
                'FIFO_eMBB', "1hop")
    write_data2(urllc_arrival_network, urllc_service_network1, urllc_service_network2, slot_num, runs, runs_blank1,
                runs_blank2, case_name, scenario_name, 'FIFO_URLLC', "2hop")
    write_data2(embb_arrival_network, urllc_service_network1, embb_service_network2, slot_num, runs, runs_blank1,
                runs_blank2, case_name, scenario_name, 'FIFO_eMBB', "2hop")
    write_backlog(backlog_runs_network1, runs, case_name, scenario_name, '1hop')
    write_backlog2(backlog_runs_network1, backlog_runs_network2, runs, case_name, scenario_name, '2hop')

    return urllc_arrival_network, urllc_service_network1, embb_arrival_network, embb_service_network1


def write_backlog(queue, runs, case_name,scenario_name, dd):
    backlog_size = 10000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (backlog_size + 1)
        delay_ccdf = [0] * backlog_size
        for time in range(len(queue[run])):
            backlog = int(queue[run][time])
            if backlog > 9999:
                backlog = 9999
            delay_list[backlog] += 1
            # print(delay_list[0])
        total = 0
        for i in range(backlog_size):
            total += delay_list[i]
        drag = total
        for i in range(backlog_size):
            delay_ccdf[i] = drag / total
            drag -= delay_list[i]
        run_data.append(delay_ccdf)

    df = pd.DataFrame(run_data)
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name+"/Simulation/" + dd + '/' + case_name + '/BACKLOG.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return None


def write_backlog2(queue1, queue2, runs, case_name, scenario_name, dd):
    backlog_size = 10000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (backlog_size + 1)
        delay_ccdf = [0] * backlog_size
        for time in range(len(queue2[run])):
            backlog = int(queue2[run][time])
            if backlog > 9999:
                backlog = 9999
            delay_list[backlog] += 1

        total = 0
        for i in range(backlog_size):
            total += delay_list[i]
        drag = total
        for i in range(backlog_size):
            delay_ccdf[i] = drag / total
            drag -= delay_list[i]
        run_data.append(delay_ccdf)

    df = pd.DataFrame(run_data)
    writer = pd.ExcelWriter(
        os.getcwd() + "/" + scenario_name+"/Simulation/" + dd + '/' + case_name + '/BACKLOG.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return None


def write_data(arrival_network, service_network, slot_num, runs, blank, case_name, scenario_name, case_d, hop):
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
        os.getcwd() + "/" + scenario_name+"/Simulation/" + hop + '/' + case_name + "/" + case_d + '.xlsx',
        engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.close()
    return None


def write_data1(arrival_network, service_network, slot_num, runs, blank, case_name, scenario_name, case_d, hop):
    delay_size = 4000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (delay_size + 1)
        delay_ccdf = [0] * delay_size
        prev = 0
        for time in range(1, slot_num + 1, 1):
            service_amount = service_network[run][time]
            while time + 1 > prev and prev < 100001:
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
        for i in range(delay_size + 1):
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


def write_data2(arrival_network, service_network1, service_network2, slot_num, runs, blank1, blank2, case_name, scenario_name, case_d,
                hop):
    delay_size = 4000
    run_data = []
    for run in range(runs):
        delay_list = [0] * (delay_size + 1)
        delay_ccdf = [0] * delay_size
        prev = 0
        for time in range(1, slot_num + 1, 1):
            service_amount = service_network2[run][time]
            while time + 1 > prev and prev < 100001:
                if arrival_network[run][prev] > service_amount:
                    break
                else:
                    prev += 1
            delay = time - prev + 1
            if delay > 4000:
                delay_list[3999] += 1
            else:
                delay_list[delay] += 1
        # prev = 0
        # for time in range(1, slot_num + 1, 1):
        #     service_amount = service_network1[run][time]
        #     while time + 1 > prev and prev < 100001:
        #         if arrival_network[run][prev] > service_amount:
        #             break
        #         else:
        #             prev += 1
        #     delay = time - prev + 1
        #     if delay > 4000:
        #         delay_list[3999] += 1
        #     else:
        #         delay_list[delay] += 1

        total = 0
        delay_list[0] -= (blank2[run])
        # delay_list[0] -= (blank2[run]+blank1[run])
        for i in range(delay_size + 1):
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
