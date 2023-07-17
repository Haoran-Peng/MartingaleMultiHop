import capacity as system_capacity
import os
import sys

def init(case, service1, service2, scenario_idx):
    case_path = ['case150x150_power20x23', 'case150x150_power30x33', 'case50x50_power20x23']
    method_path = ['Martingale', 'Simulation', "SNC"]
    hop_path = ['1hop', '2hop']
    case_name = ['MISO', 'DF25', 'DF100', 'RIS25', 'RIS100']

    for a in range(len(case_path)):
        for b in range(len(method_path)):
            for c in range(len(hop_path)):
                for d in range(len(case_name)):
                    path = case_path[a]+'/'+method_path[b]+'/'+hop_path[c]+'/'+case_name[d]
                    isExist = os.path.exists(path)
                    if not isExist:
                        # Create a new directory because it does not exist
                        os.makedirs(path)
    if scenario_idx == 0:
        capacity = system_capacity.maximum_transmission_rate(150, 150, 20, 23)
    if scenario_idx == 1:
        capacity = system_capacity.maximum_transmission_rate(150, 150, 30, 33)
    if scenario_idx == 2:
        capacity = system_capacity.maximum_transmission_rate(50, 50, 20, 23)
    # standardization_URLLC_rate = 0.1
    standardization_eMBB_rate = 0.01
    print(capacity)
    # 讓不同情境下的抵達機率標準化
    standardization_time_slot = 0.027
    time_slot = round(32 * 8 / (capacity[case] / 5 / 1000), 8)
    eMBB_arrival_rate = round(standardization_eMBB_rate * time_slot / standardization_time_slot, 8)
    print("here",0.1*standardization_eMBB_rate/standardization_time_slot)
    # URLLC 是 eMBB 抵達率的十倍
    URLLC_arrival_rate = eMBB_arrival_rate * 10
    print(eMBB_arrival_rate*50*6+URLLC_arrival_rate*1*12, "time_slot : ",time_slot)  #need to satisfied stable condition
    if eMBB_arrival_rate*50*6+URLLC_arrival_rate*1*12>4:
        print('not satisfied stable condition')
        sys.exit()
    print("eMBB_arrival_rate : ",eMBB_arrival_rate, "URLLC_arrival_rate",URLLC_arrival_rate)
    eta = (1 / service1) / (1 / service2 + 1 / service1)

    # subtract the requirement with the transmission time
    EDF_param1 = round((25 - 2 - time_slot * 9 + 0.5) / time_slot)
    EDF_param2 = round((25 - 2 - time_slot * 20.5 + 0.5) / time_slot)

    return capacity, time_slot, URLLC_arrival_rate, eMBB_arrival_rate, eta, EDF_param1, EDF_param2
