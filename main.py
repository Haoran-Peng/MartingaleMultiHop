import random
import copy
import numpy as np
# import create_data as create
import data_init as data_initialize
import matrix_init as matrix_initialize

import create_data as create
import martingale_1hop_analysis as mta1
import martingale_2hop_analysis as mta2
import stochastic_network_1hop_analysis as snca1
import stochastic_network_2hop_analysis as snca2
import nonpreemptive_12hop_simulation as nps12
import preemptive_12hop_simulation as ps12
import edf_1hop_simulation as edfs1
import edf_2hop_simulation as edfs2

if __name__ == "__main__":
    random.seed(27)

    URLLC_resource_block = 1
    eMBB_resource_block = 50

    URLLC_process_num = 12
    eMBB_process_num = 6

    simulate_slot_num = 100000
    simulate_run = 30

    service1_resource_block = 5
    service2_resource_block = 4

    service1_rate = 1.0
    service2_rate = 1.0

    # case 1,2,3,4, 5 represent the MISO, single_DF, multi_DF, RIS25 and RIS100 initialize process
    
    case_name = ['MISO', 'DF25', 'DF100', 'RIS25', 'RIS100']
    
    scenario_name = ['case150x150_power20x23', 'case150x150_power30x33', 'case50x50_power20x23']
    
    for i in range(0,len(case_name)):
        for j in range(0, len(scenario_name)):
            print("Case: "+case_name[i])
            print("Scenario: "+scenario_name[j])
            case_idx = i
            scenario_idx = j
            capacity, time_slot, URLLC_arrival_rate, eMBB_arrival_rate, eta, EDF_param1, EDF_param2 = data_initialize.init(case_idx, service1_resource_block, service2_resource_block, scenario_idx)

            URLLC_markov_mat, eMBB_markov_mat, service1_markov_mat, service2_markov_mat, URLLC_steady_vec, eMBB_steady_vec, service1_steady_vec, service2_steady_vec = matrix_initialize.init(
                URLLC_arrival_rate, eMBB_arrival_rate, service1_rate, service2_rate)

            # all scheduling policy mathematics bound

            # 1 hop martingale
            mta1.analyze(URLLC_markov_mat, URLLC_resource_block, URLLC_process_num, URLLC_steady_vec, eMBB_markov_mat,
                         eMBB_resource_block, eMBB_process_num, eMBB_steady_vec, service1_markov_mat, service1_resource_block,
                         service1_steady_vec, EDF_param1, time_slot, case_name[case_idx], scenario_name[scenario_idx])
            
            # 2 hop martingale
            mta2.analyze(URLLC_markov_mat, URLLC_resource_block, URLLC_process_num, URLLC_steady_vec, eMBB_markov_mat,
                         eMBB_resource_block, eMBB_process_num, eMBB_steady_vec, service1_markov_mat, service2_markov_mat,
                         service1_resource_block, service2_resource_block, service1_steady_vec, service2_steady_vec, EDF_param2,
                         time_slot, case_name[case_idx],scenario_name[scenario_idx], eta)

            # 1 hop stochastic network calculus
            snca1.analyze(URLLC_markov_mat, URLLC_resource_block, URLLC_process_num, eMBB_markov_mat,
                          eMBB_resource_block, eMBB_process_num, service1_markov_mat, service1_resource_block,
                          EDF_param1, time_slot, case_name[case_idx],scenario_name[scenario_idx])

            # 2 hop stochastic network calculus
            snca2.analyze(URLLC_markov_mat, URLLC_resource_block, URLLC_process_num, eMBB_markov_mat,
                          eMBB_resource_block, eMBB_process_num, service1_markov_mat, service2_markov_mat,
                          service1_resource_block, service2_resource_block,
                          EDF_param2, time_slot, case_name[case_idx],scenario_name[scenario_idx], eta)

            # # create the simulation data
            URLLC_arrival_process, eMBB_arrival_process = create.create_data(URLLC_arrival_rate, eMBB_arrival_rate,
                                                                             URLLC_process_num, eMBB_process_num,
                                                                             simulate_slot_num, simulate_run)

            # non-preemptive 1 and 2 hop simulation of the delay and backlog

            up = copy.deepcopy(URLLC_arrival_process)
            ep = copy.deepcopy(eMBB_arrival_process)
            nps12.simulation(up, ep, URLLC_resource_block, eMBB_resource_block,
                             service1_markov_mat, service1_resource_block, service2_markov_mat, service2_resource_block,
                             simulate_slot_num, simulate_run, case_name[case_idx], scenario_name[scenario_idx])
            print("finish fifo")

            up = copy.deepcopy(URLLC_arrival_process)
            ep = copy.deepcopy(eMBB_arrival_process)

            # preemptive 1 and 2 hop simulation of the delay

            ps12.simulation(up, ep, URLLC_resource_block, eMBB_resource_block,
                            service1_markov_mat, service1_resource_block, service2_markov_mat, service2_resource_block,
                            simulate_slot_num, simulate_run, case_name[case_idx], scenario_name[scenario_idx])
            print("finish sp")

            up = copy.deepcopy(URLLC_arrival_process)
            ep = copy.deepcopy(eMBB_arrival_process)

            # edf 1 hop simulation of the delay

            edfs1.simulation(up, ep, URLLC_resource_block, eMBB_resource_block, service1_markov_mat, service1_resource_block,
                             service2_markov_mat, service2_resource_block, EDF_param1, simulate_slot_num,
                             simulate_run, case_name[case_idx], scenario_name[scenario_idx])

            up = copy.deepcopy(URLLC_arrival_process)
            ep = copy.deepcopy(eMBB_arrival_process)

            # edf 2 hop simulation of the delay

            edfs2.simulation(up, ep, URLLC_resource_block, eMBB_resource_block, service1_markov_mat, service1_resource_block,
                             service2_markov_mat, service2_resource_block, EDF_param2, simulate_slot_num,
                             simulate_run, case_name[case_idx], scenario_name[scenario_idx])

            print("finish edf")
