import math

import numpy as np
from rftool.utility import *
from numpy import linalg as LA


def pathloss_3GPP_LOS(fc, x):
    return db2pow(-28 - 20 * math.log10(fc) - 22 * math.log10(x))


def pathloss_3GPP_NLOS(fc, x):
    return db2pow(-22.7 - 26 * math.log10(fc) - 36.7 * math.log10(x))


def maximum_transmission_rate(d_br, d_rv, power1, power2):
    # Carrier fequency (in GHz)
    fc = 3

    # Bandwidth (in hz)
    B = 900000

    # Noise figure (in dB)
    noiseFiguredB = 10
    interbeam_interferencedB = 12.3
    # Calculate the noise (in dbm)
    sigma2dBm_interference = -174 + 10 * math.log10(900000) + noiseFiguredB + interbeam_interferencedB # ~= -104dbm
    print(sigma2dBm_interference)
    # Convert the noise/ antennaGain to power
    sigma2 = db2pow(sigma2dBm_interference)
    antennaGainB = db2pow(5)
    antennaGainR = db2pow(5)
    antennaGainU = db2pow(0)

    BR_antenna_num = 18 # bs and receiver amount
    # RIS reflect factor
    alpha = 1

    # distance between base-station, ris, and receiver
    # d_br = 50
    # d_rv = 20
    d_bv = math.sqrt(d_br ** 2 + d_rv ** 2)
    print(d_bv)
    RIS_amount = [25, 100]

    # pathloss of the channel
    betaBR = np.sqrt(pathloss_3GPP_LOS(fc, d_br) * antennaGainB * antennaGainR)
    betaBU = np.sqrt(pathloss_3GPP_NLOS(fc, d_bv) * antennaGainB * antennaGainU)
    betaRU = np.sqrt(pathloss_3GPP_LOS(fc, d_rv) * antennaGainR * antennaGainU)
    #

    # base-station transmit power and convert to power
    print(10**(10/10))
    p_u_dbm = power1
    p_u = 10 ** (p_u_dbm / 10)
    p_e_dbm = power2
    p_e = 10 ** (p_e_dbm / 10)
    p_m = []
    for i in range(12):
        p_m.append(p_u)
    for i in range(6):
        p_m.append(p_e)

    p_m = np.array(p_m)
    p_m = np.expand_dims(p_m, axis=1)
    p_m = np.squeeze(p_m, axis=1)
    p_m = np.diag(p_m)
    # calculate the MISO capacity

    # assume bs has 5 antennas
    H_BU = []
    for i in range(BR_antenna_num):
        beta_bu = []
        for j in range(BR_antenna_num):
            beta_bu.append(betaBU)
        H_BU.append(beta_bu)
    H_BU = np.array(H_BU)
    H_BU = np.expand_dims(H_BU, axis=1)
    H_BU = np.squeeze(H_BU, axis=1)

    # MRT precoding
    w = np.conjugate(H_BU) / LA.norm(H_BU)
    capacity_MISO2 = np.trace(B * (np.log2(1 + p_m @ w @ H_BU @ H_BU.T / sigma2)))
    # calculate the RIS capacity

    H_BR_RIS1 = []
    H_BR_RIS2 = []
    H_RU_RIS1 = []
    H_RU_RIS2 = []
    for i in range(25):
        beta_br = []
        beta_ru = []
        for j in range(BR_antenna_num):
            beta_br.append(betaBR)
            beta_ru.append(betaRU)
        H_BR_RIS1.append(beta_br)
        H_RU_RIS1.append(beta_ru)

    H_BR_RIS1 = np.array(H_BR_RIS1)
    H_BR_RIS1 = np.expand_dims(H_BR_RIS1, axis=2)
    H_BR_RIS1 = np.squeeze(H_BR_RIS1, axis=2)
    H_RU_RIS1 = np.array(H_RU_RIS1)
    H_RU_RIS1 = np.expand_dims(H_RU_RIS1, axis=2)
    H_RU_RIS1 = np.squeeze(H_RU_RIS1, axis=2)
    for i in range(100):
        beta_br = []
        beta_ru = []
        for j in range(BR_antenna_num):
            beta_br.append(betaBR)
            beta_ru.append(betaRU)
        H_BR_RIS2.append(beta_br)
        H_RU_RIS2.append(beta_ru)
    H_BR_RIS2 = np.array(H_BR_RIS2)
    H_BR_RIS2 = np.expand_dims(H_BR_RIS2, axis=2)
    H_BR_RIS2 = np.squeeze(H_BR_RIS2, axis=2)
    H_RU_RIS2 = np.array(H_RU_RIS2)
    H_RU_RIS2 = np.expand_dims(H_RU_RIS2, axis=2)
    H_RU_RIS2 = np.squeeze(H_RU_RIS2, axis=2)
    # print(H_RU_RIS2.shape, H_BR_RIS2.shape)

    capacity_RIS1 = [0, 0]
    # # https://arxiv.org/pdf/2002.04960.pdf eq 42 #
    capacity_RIS1[0] = np.trace(
        B * np.log2(1 + p_m @ np.add(w @ H_BU.T, w @ H_RU_RIS1.T @ H_BR_RIS1) @ np.add(w @ H_BU.T,
                                                                                       w @ H_RU_RIS1.T @ H_BR_RIS1).T / sigma2))
    capacity_RIS1[1] = np.trace(
        B * np.log2(1 + p_m @ np.add(w @ H_BU.T, w @ H_RU_RIS2.T @ H_BR_RIS2) @ np.add(w @ H_BU.T,
                                                                                       w @ H_RU_RIS2.T @ H_BR_RIS2).T / sigma2))
    capacity_DF = [0, 0]

    # single antenna relay
    Relay_antenna_num = 25
    H_BR_Relay = []
    H_RU_Relay = []
    for i in range(Relay_antenna_num):
        beta_br = []
        beta_ru = []
        for j in range(BR_antenna_num):
            beta_br.append(betaBR)
            beta_ru.append(betaRU)
        H_BR_Relay.append(beta_br)
        H_RU_Relay.append(beta_ru)
    H_BR_Relay = np.array(H_BR_Relay)
    H_BR_Relay = np.expand_dims(H_BR_Relay, axis=2)
    H_BR_Relay = np.squeeze(H_BR_Relay, axis=2)
    H_RU_Relay = np.array(H_RU_Relay)
    H_RU_Relay = np.expand_dims(H_RU_Relay, axis=2)
    H_RU_Relay = np.squeeze(H_RU_Relay, axis=2)

    # D_BR = (H_BR_Relay.T@H_BR_Relay)[0][0]
    # D_BU = (H_BU.T@H_BU)[0][0]
    # D_RU = (H_RU_Relay.T@H_RU_Relay)[0][0]
    # print(D_BR)

    stage_1 = np.trace(1 / 2 * B * np.log2(1 + p_m @ H_BR_Relay.T @ H_BR_Relay / sigma2))
    stage_2 = np.trace(
        1 / 2 * B * np.log2(1 + p_m @ w @ H_BU.T @ H_BU / sigma2 + p_m @ w @ H_RU_Relay.T @ H_RU_Relay / sigma2))
    # stage_2 = p * H_BU.T@H_BU / sigma2 + p * (np.dot(H_RU_Relay.T, H_RU_Relay))) / sigma2)
    # print(np.add(p*H_BU.T@H_BU+p * H_RU_Relay.T@H_RU_Relay))
    capacity_DF[0] = min(stage_1, stage_2)

    # print(D_BR, D_BU, D_RU)
    # if D_BR >= D_BU:
    #     capacity_DF[0] = 1 / 2 * B * np.log2(1 + (2 * p * D_RU * D_BR) / (D_BR + D_RU - D_BU) / sigma2)
    # else:
    #     capacity_DF[0] = B * (math.log2(1 + 2 * p * D_BU / sigma2))
    # print(stage_1, stage_2)
    # multi antenna relay
    # calculate the DF capacity

    Relay_antenna_num = 100
    H_BR_Relay = []
    H_RU_Relay = []
    for i in range(Relay_antenna_num):
        beta_br = []
        beta_ru = []
        for j in range(BR_antenna_num):
            beta_br.append(betaBR)
            beta_ru.append(betaRU)
        H_BR_Relay.append(beta_br)
        H_RU_Relay.append(beta_ru)
    H_BR_Relay = np.array(H_BR_Relay)
    H_BR_Relay = np.expand_dims(H_BR_Relay, axis=2)
    H_BR_Relay = np.squeeze(H_BR_Relay, axis=2)
    H_RU_Relay = np.array(H_RU_Relay)
    H_RU_Relay = np.expand_dims(H_RU_Relay, axis=2)
    H_RU_Relay = np.squeeze(H_RU_Relay, axis=2)

    stage_1 = np.trace(1 / 2 * B * np.log2(1 + p_m @ H_BR_Relay.T @ H_BR_Relay / sigma2))
    stage_2 = np.trace(
        1 / 2 * B * np.log2(1 + p_m @ w @ H_BU.T @ H_BU / sigma2 + p_m @ w @ H_RU_Relay.T @ H_RU_Relay / sigma2))
    capacity_DF[1] = min(stage_1, stage_2)

    print(stage_1)
    capacity_return = [capacity_MISO2, capacity_DF[0], capacity_DF[1], capacity_RIS1[0], capacity_RIS1[1]]
    return capacity_return


if __name__ == "__main__":
    capacity = maximum_transmission_rate(50, 50)  # Example with 2 antennas
    print(capacity)
