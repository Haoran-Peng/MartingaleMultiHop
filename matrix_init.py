import numpy as np


def init(URLLC_arrival_rate, eMBB_arrival_rate, service1_arrival_rate, service2_arrival_rate):
    URLLC_markov_mat = np.array(
        [[1 - URLLC_arrival_rate, URLLC_arrival_rate], [1 - URLLC_arrival_rate, URLLC_arrival_rate]], np.float64)
    eMBB_markov_mat = np.array([[1 - eMBB_arrival_rate, eMBB_arrival_rate], [1 - eMBB_arrival_rate, eMBB_arrival_rate]],
                               np.float64)
    service1_markov_mat = np.array(
        [[1 - service1_arrival_rate, service1_arrival_rate], [1 - service1_arrival_rate, service1_arrival_rate]],
        np.float64)
    service2_markov_mat = np.array(
        [[1 - service2_arrival_rate, service2_arrival_rate], [1 - service2_arrival_rate, service2_arrival_rate]],
        np.float64)
    URLLC_steady_vec = np.array([1 - URLLC_arrival_rate, URLLC_arrival_rate], np.float64)
    eMBB_steady_vec = np.array([1 - eMBB_arrival_rate, eMBB_arrival_rate], np.float64)
    service1_steady_vec = np.array([1 - service1_arrival_rate, service1_arrival_rate], np.float64)
    service2_steady_vec = np.array([1 - service2_arrival_rate, service2_arrival_rate], np.float64)

    return URLLC_markov_mat,  eMBB_markov_mat, service1_markov_mat, service2_markov_mat, URLLC_steady_vec, eMBB_steady_vec, service1_steady_vec, service2_steady_vec
