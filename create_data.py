import random
import numpy as np


def create_data(URLLC_arrival_rate, eMBB_arrival_rate, URLLC_process_num, eMBB_process_num, simulate_slot_num, simulate_runs):
    print('\n==== Creating URLLC and eMBB data ====\n')

    URLLC_arrivals = np.zeros([simulate_runs, simulate_slot_num + 1])
    eMBB_arrivals = np.zeros([simulate_runs, simulate_slot_num + 1])

    URLLC_non_arrive_prob = (1 - URLLC_arrival_rate) * 100000000
    eMBB_non_arrive_prob = (1 - eMBB_arrival_rate) * 100000000

    for run in range(simulate_runs):
        for time in range(1, simulate_slot_num + 1, 1):
            URLLC_each_time_arrivals = 0
            eMBB_each_time_arrivals = 0
            for i in range(URLLC_process_num):
                tc_arrival_prob = random.randint(1, 100000000)
                if URLLC_non_arrive_prob < tc_arrival_prob:
                    URLLC_each_time_arrivals += 1
            for i in range(eMBB_process_num):
                eb_arrival_prob = random.randint(1, 100000000)
                if eMBB_non_arrive_prob < eb_arrival_prob:
                    eMBB_each_time_arrivals += 1
            URLLC_arrivals[run][time] += URLLC_each_time_arrivals
            eMBB_arrivals[run][time] += eMBB_each_time_arrivals
    print("\n==== creation done ====\n")
    return URLLC_arrivals, eMBB_arrivals
