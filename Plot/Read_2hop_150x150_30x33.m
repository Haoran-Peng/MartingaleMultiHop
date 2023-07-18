% Read MIMO data
MT_2hop_MISO_URLLC_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\EDF_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_URLLC_EDF_A2  = table2array(MT_2hop_MISO_URLLC_EDF);
SIM_2hop_MISO_URLLC_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_URLLC_EDF_A2  = table2array(SIM_2hop_MISO_URLLC_EDF);
SNC_2hop_MISO_URLLC_EDF = readtable('..\case150x150_power30x33\SNC\2hop\MISO\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_URLLC_EDF_A2  = table2array(SNC_2hop_MISO_URLLC_EDF);

MT_2hop_MISO_EMBB_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\EDF_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_EMBB_EDF_A2  = table2array(MT_2hop_MISO_EMBB_EDF);
SIM_2hop_MISO_EMBB_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_EMBB_EDF_A2  = table2array(SIM_2hop_MISO_EMBB_EDF);
SNC_2hop_MISO_EMBB_EDF = readtable('..\case150x150_power30x33\SNC\2hop\MISO\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_EMBB_EDF_A2  = table2array(SNC_2hop_MISO_EMBB_EDF);

MT_2hop_MISO_URLLC_SP = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\SP_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_URLLC_SP_A2  = table2array(MT_2hop_MISO_URLLC_SP);
SIM_2hop_MISO_URLLC_SP = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\SP_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_URLLC_SP_A2  = table2array(SIM_2hop_MISO_URLLC_SP);
SNC_2hop_MISO_URLLC_SP = readtable('..\case150x150_power30x33\SNC\2hop\MISO\SP_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_URLLC_SP_A2  = table2array(SNC_2hop_MISO_URLLC_SP);

MT_2hop_MISO_EMBB_SP = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\SP_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_EMBB_SP_A2  = table2array(MT_2hop_MISO_EMBB_SP);
SIM_2hop_MISO_EMBB_SP = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\SP_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_EMBB_SP_A2  = table2array(SIM_2hop_MISO_EMBB_SP);
SNC_2hop_MISO_EMBB_SP = readtable('..\case150x150_power30x33\SNC\2hop\MISO\SP_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_EMBB_SP_A2  = table2array(SNC_2hop_MISO_EMBB_SP);

MT_2hop_MISO_URLLC_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_URLLC_FIFO_A2  = table2array(MT_2hop_MISO_URLLC_FIFO);
SIM_2hop_MISO_URLLC_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\FIFO_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_URLLC_FIFO_A2  = table2array(SIM_2hop_MISO_URLLC_FIFO);
SNC_2hop_MISO_URLLC_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\MISO\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_URLLC_FIFO_A2  = table2array(SNC_2hop_MISO_URLLC_FIFO);

MT_2hop_MISO_EMBB_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_EMBB_FIFO_A2  = table2array(MT_2hop_MISO_EMBB_FIFO);
SIM_2hop_MISO_EMBB_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\FIFO_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_EMBB_FIFO_A2  = table2array(SIM_2hop_MISO_EMBB_FIFO);
SNC_2hop_MISO_EMBB_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\MISO\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_EMBB_FIFO_A2  = table2array(SNC_2hop_MISO_EMBB_SP);

MT_2hop_MISO_BACKLOG = readtable('..\case150x150_power30x33\Martingale\2hop\MISO\BACKLOG.xlsx', 'NumHeaderLines',1);
MT_2hop_MISO_BACKLOG_A2  = table2array(MT_2hop_MISO_BACKLOG);
SIM_2hop_MISO_BACKLOG = readtable('..\case150x150_power30x33\Simulation\2hop\MISO\BACKLOG.xlsx', 'NumHeaderLines',1);
SIM_2hop_MISO_BACKLOG_A2  = table2array(SIM_2hop_MISO_BACKLOG);
SNC_2hop_MISO_BACKLOG = readtable('..\case150x150_power30x33\SNC\2hop\MISO\BACKLOG.xlsx', 'NumHeaderLines',1);
SNC_2hop_MISO_BACKLOG_A2  = table2array(SNC_2hop_MISO_BACKLOG);



% Read DF25 data
MT_2hop_DF25_URLLC_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\EDF_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_URLLC_EDF_A2  = table2array(MT_2hop_DF25_URLLC_EDF);
SIM_2hop_DF25_URLLC_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_URLLC_EDF_A2  = table2array(SIM_2hop_DF25_URLLC_EDF);
SNC_2hop_DF25_URLLC_EDF = readtable('..\case150x150_power30x33\SNC\2hop\DF25\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_URLLC_EDF_A2  = table2array(SNC_2hop_DF25_URLLC_EDF);

MT_2hop_DF25_EMBB_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\EDF_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_EMBB_EDF_A2  = table2array(MT_2hop_DF25_EMBB_EDF);
SIM_2hop_DF25_EMBB_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_EMBB_EDF_A2  = table2array(SIM_2hop_DF25_EMBB_EDF);
SNC_2hop_DF25_EMBB_EDF = readtable('..\case150x150_power30x33\SNC\2hop\DF25\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_EMBB_EDF_A2  = table2array(SNC_2hop_DF25_EMBB_EDF);

MT_2hop_DF25_URLLC_SP = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\SP_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_URLLC_SP_A2  = table2array(MT_2hop_DF25_URLLC_SP);
SIM_2hop_DF25_URLLC_SP = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\SP_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_URLLC_SP_A2  = table2array(SIM_2hop_DF25_URLLC_SP);
SNC_2hop_DF25_URLLC_SP = readtable('..\case150x150_power30x33\SNC\2hop\DF25\SP_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_URLLC_SP_A2  = table2array(SNC_2hop_DF25_URLLC_SP);

MT_2hop_DF25_EMBB_SP = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\SP_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_EMBB_SP_A2  = table2array(MT_2hop_DF25_EMBB_SP);
SIM_2hop_DF25_EMBB_SP = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\SP_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_EMBB_SP_A2  = table2array(SIM_2hop_DF25_EMBB_SP);
SNC_2hop_DF25_EMBB_SP = readtable('..\case150x150_power30x33\SNC\2hop\DF25\SP_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_EMBB_SP_A2  = table2array(SNC_2hop_DF25_EMBB_SP);

MT_2hop_DF25_URLLC_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_URLLC_FIFO_A2  = table2array(MT_2hop_DF25_URLLC_FIFO);
SIM_2hop_DF25_URLLC_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\FIFO_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_URLLC_FIFO_A2  = table2array(SIM_2hop_DF25_URLLC_FIFO);
SNC_2hop_DF25_URLLC_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\DF25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_URLLC_FIFO_A2  = table2array(SNC_2hop_DF25_URLLC_FIFO);

MT_2hop_DF25_EMBB_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_EMBB_FIFO_A2  = table2array(MT_2hop_DF25_EMBB_FIFO);
SIM_2hop_DF25_EMBB_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\FIFO_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_EMBB_FIFO_A2  = table2array(SIM_2hop_DF25_EMBB_FIFO);
SNC_2hop_DF25_EMBB_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\DF25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_EMBB_FIFO_A2  = table2array(SNC_2hop_DF25_EMBB_SP);

MT_2hop_DF25_BACKLOG = readtable('..\case150x150_power30x33\Martingale\2hop\DF25\BACKLOG.xlsx', 'NumHeaderLines',1);
MT_2hop_DF25_BACKLOG_A2  = table2array(MT_2hop_DF25_BACKLOG);
SIM_2hop_DF25_BACKLOG = readtable('..\case150x150_power30x33\Simulation\2hop\DF25\BACKLOG.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF25_BACKLOG_A2  = table2array(SIM_2hop_DF25_BACKLOG);
SNC_2hop_DF25_BACKLOG = readtable('..\case150x150_power30x33\SNC\2hop\DF25\BACKLOG.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF25_BACKLOG_A2  = table2array(SNC_2hop_DF25_BACKLOG);



% Read DF100 data
MT_2hop_DF100_URLLC_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\EDF_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_URLLC_EDF_A2  = table2array(MT_2hop_DF100_URLLC_EDF);
SIM_2hop_DF100_URLLC_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_URLLC_EDF_A2  = table2array(SIM_2hop_DF100_URLLC_EDF);
SNC_2hop_DF100_URLLC_EDF = readtable('..\case150x150_power30x33\SNC\2hop\DF100\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_URLLC_EDF_A2  = table2array(SNC_2hop_DF100_URLLC_EDF);

MT_2hop_DF100_EMBB_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\EDF_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_EMBB_EDF_A2  = table2array(MT_2hop_DF100_EMBB_EDF);
SIM_2hop_DF100_EMBB_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_EMBB_EDF_A2  = table2array(SIM_2hop_DF100_EMBB_EDF);
SNC_2hop_DF100_EMBB_EDF = readtable('..\case150x150_power30x33\SNC\2hop\DF100\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_EMBB_EDF_A2  = table2array(SNC_2hop_DF100_EMBB_EDF);

MT_2hop_DF100_URLLC_SP = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\SP_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_URLLC_SP_A2  = table2array(MT_2hop_DF100_URLLC_SP);
SIM_2hop_DF100_URLLC_SP = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\SP_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_URLLC_SP_A2  = table2array(SIM_2hop_DF100_URLLC_SP);
SNC_2hop_DF100_URLLC_SP = readtable('..\case150x150_power30x33\SNC\2hop\DF100\SP_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_URLLC_SP_A2  = table2array(SNC_2hop_DF100_URLLC_SP);

MT_2hop_DF100_EMBB_SP = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\SP_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_EMBB_SP_A2  = table2array(MT_2hop_DF100_EMBB_SP);
SIM_2hop_DF100_EMBB_SP = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\SP_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_EMBB_SP_A2  = table2array(SIM_2hop_DF100_EMBB_SP);
SNC_2hop_DF100_EMBB_SP = readtable('..\case150x150_power30x33\SNC\2hop\DF100\SP_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_EMBB_SP_A2  = table2array(SNC_2hop_DF100_EMBB_SP);

MT_2hop_DF100_URLLC_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_URLLC_FIFO_A2  = table2array(MT_2hop_DF100_URLLC_FIFO);
SIM_2hop_DF100_URLLC_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\FIFO_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_URLLC_FIFO_A2  = table2array(SIM_2hop_DF100_URLLC_FIFO);
SNC_2hop_DF100_URLLC_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\DF100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_URLLC_FIFO_A2  = table2array(SNC_2hop_DF100_URLLC_FIFO);

MT_2hop_DF100_EMBB_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_EMBB_FIFO_A2  = table2array(MT_2hop_DF100_EMBB_FIFO);
SIM_2hop_DF100_EMBB_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\FIFO_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_EMBB_FIFO_A2  = table2array(SIM_2hop_DF100_EMBB_FIFO);
SNC_2hop_DF100_EMBB_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\DF100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_EMBB_FIFO_A2  = table2array(SNC_2hop_DF100_EMBB_SP);

MT_2hop_DF100_BACKLOG = readtable('..\case150x150_power30x33\Martingale\2hop\DF100\BACKLOG.xlsx', 'NumHeaderLines',1);
MT_2hop_DF100_BACKLOG_A2  = table2array(MT_2hop_DF100_BACKLOG);
SIM_2hop_DF100_BACKLOG = readtable('..\case150x150_power30x33\Simulation\2hop\DF100\BACKLOG.xlsx', 'NumHeaderLines',1);
SIM_2hop_DF100_BACKLOG_A2  = table2array(SIM_2hop_DF100_BACKLOG);
SNC_2hop_DF100_BACKLOG = readtable('..\case150x150_power30x33\SNC\2hop\DF100\BACKLOG.xlsx', 'NumHeaderLines',1);
SNC_2hop_DF100_BACKLOG_A2  = table2array(SNC_2hop_DF100_BACKLOG);


% Read RIS25 data
MT_2hop_RIS25_URLLC_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\EDF_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_URLLC_EDF_A2  = table2array(MT_2hop_RIS25_URLLC_EDF);
SIM_2hop_RIS25_URLLC_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_URLLC_EDF_A2  = table2array(SIM_2hop_RIS25_URLLC_EDF);
SNC_2hop_RIS25_URLLC_EDF = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_URLLC_EDF_A2  = table2array(SNC_2hop_RIS25_URLLC_EDF);

MT_2hop_RIS25_EMBB_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\EDF_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_EMBB_EDF_A2  = table2array(MT_2hop_RIS25_EMBB_EDF);
SIM_2hop_RIS25_EMBB_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_EMBB_EDF_A2  = table2array(SIM_2hop_RIS25_EMBB_EDF);
SNC_2hop_RIS25_EMBB_EDF = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_EMBB_EDF_A2  = table2array(SNC_2hop_RIS25_EMBB_EDF);

MT_2hop_RIS25_URLLC_SP = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\SP_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_URLLC_SP_A2  = table2array(MT_2hop_RIS25_URLLC_SP);
SIM_2hop_RIS25_URLLC_SP = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\SP_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_URLLC_SP_A2  = table2array(SIM_2hop_RIS25_URLLC_SP);
SNC_2hop_RIS25_URLLC_SP = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\SP_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_URLLC_SP_A2  = table2array(SNC_2hop_RIS25_URLLC_SP);

MT_2hop_RIS25_EMBB_SP = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\SP_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_EMBB_SP_A2  = table2array(MT_2hop_RIS25_EMBB_SP);
SIM_2hop_RIS25_EMBB_SP = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\SP_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_EMBB_SP_A2  = table2array(SIM_2hop_RIS25_EMBB_SP);
SNC_2hop_RIS25_EMBB_SP = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\SP_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_EMBB_SP_A2  = table2array(SNC_2hop_RIS25_EMBB_SP);

MT_2hop_RIS25_URLLC_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_URLLC_FIFO_A2  = table2array(MT_2hop_RIS25_URLLC_FIFO);
SIM_2hop_RIS25_URLLC_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\FIFO_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_URLLC_FIFO_A2  = table2array(SIM_2hop_RIS25_URLLC_FIFO);
SNC_2hop_RIS25_URLLC_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_URLLC_FIFO_A2  = table2array(SNC_2hop_RIS25_URLLC_FIFO);

MT_2hop_RIS25_EMBB_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_EMBB_FIFO_A2  = table2array(MT_2hop_RIS25_EMBB_FIFO);
SIM_2hop_RIS25_EMBB_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\FIFO_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_EMBB_FIFO_A2  = table2array(SIM_2hop_RIS25_EMBB_FIFO);
SNC_2hop_RIS25_EMBB_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_EMBB_FIFO_A2  = table2array(SNC_2hop_RIS25_EMBB_SP);

MT_2hop_RIS25_BACKLOG = readtable('..\case150x150_power30x33\Martingale\2hop\RIS25\BACKLOG.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS25_BACKLOG_A2  = table2array(MT_2hop_RIS25_BACKLOG);
SIM_2hop_RIS25_BACKLOG = readtable('..\case150x150_power30x33\Simulation\2hop\RIS25\BACKLOG.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS25_BACKLOG_A2  = table2array(SIM_2hop_RIS25_BACKLOG);
SNC_2hop_RIS25_BACKLOG = readtable('..\case150x150_power30x33\SNC\2hop\RIS25\BACKLOG.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS25_BACKLOG_A2  = table2array(SNC_2hop_RIS25_BACKLOG);


% Read RIS100 data
MT_2hop_RIS100_URLLC_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\EDF_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_URLLC_EDF_A2  = table2array(MT_2hop_RIS100_URLLC_EDF);
SIM_2hop_RIS100_URLLC_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_URLLC_EDF_A2  = table2array(SIM_2hop_RIS100_URLLC_EDF);
SNC_2hop_RIS100_URLLC_EDF = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\EDF_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_URLLC_EDF_A2  = table2array(SNC_2hop_RIS100_URLLC_EDF);

MT_2hop_RIS100_EMBB_EDF = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\EDF_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_EMBB_EDF_A2  = table2array(MT_2hop_RIS100_EMBB_EDF);
SIM_2hop_RIS100_EMBB_EDF = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_EMBB_EDF_A2  = table2array(SIM_2hop_RIS100_EMBB_EDF);
SNC_2hop_RIS100_EMBB_EDF = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\EDF_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_EMBB_EDF_A2  = table2array(SNC_2hop_RIS100_EMBB_EDF);

MT_2hop_RIS100_URLLC_SP = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\SP_URLLC.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_URLLC_SP_A2  = table2array(MT_2hop_RIS100_URLLC_SP);
SIM_2hop_RIS100_URLLC_SP = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\SP_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_URLLC_SP_A2  = table2array(SIM_2hop_RIS100_URLLC_SP);
SNC_2hop_RIS100_URLLC_SP = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\SP_URLLC.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_URLLC_SP_A2  = table2array(SNC_2hop_RIS100_URLLC_SP);

MT_2hop_RIS100_EMBB_SP = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\SP_eMBB.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_EMBB_SP_A2  = table2array(MT_2hop_RIS100_EMBB_SP);
SIM_2hop_RIS100_EMBB_SP = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\SP_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_EMBB_SP_A2  = table2array(SIM_2hop_RIS100_EMBB_SP);
SNC_2hop_RIS100_EMBB_SP = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\SP_eMBB.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_EMBB_SP_A2  = table2array(SNC_2hop_RIS100_EMBB_SP);

MT_2hop_RIS100_URLLC_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_URLLC_FIFO_A2  = table2array(MT_2hop_RIS100_URLLC_FIFO);
SIM_2hop_RIS100_URLLC_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\FIFO_URLLC.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_URLLC_FIFO_A2  = table2array(SIM_2hop_RIS100_URLLC_FIFO);
SNC_2hop_RIS100_URLLC_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_URLLC_FIFO_A2  = table2array(SNC_2hop_RIS100_URLLC_FIFO);

MT_2hop_RIS100_EMBB_FIFO = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_EMBB_FIFO_A2  = table2array(MT_2hop_RIS100_EMBB_FIFO);
SIM_2hop_RIS100_EMBB_FIFO = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\FIFO_eMBB.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_EMBB_FIFO_A2  = table2array(SIM_2hop_RIS100_EMBB_FIFO);
SNC_2hop_RIS100_EMBB_FIFO = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\FIFO_BOTH.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_EMBB_FIFO_A2  = table2array(SNC_2hop_RIS100_EMBB_SP);

MT_2hop_RIS100_BACKLOG = readtable('..\case150x150_power30x33\Martingale\2hop\RIS100\BACKLOG.xlsx', 'NumHeaderLines',1);
MT_2hop_RIS100_BACKLOG_A2  = table2array(MT_2hop_RIS100_BACKLOG);
SIM_2hop_RIS100_BACKLOG = readtable('..\case150x150_power30x33\Simulation\2hop\RIS100\BACKLOG.xlsx', 'NumHeaderLines',1);
SIM_2hop_RIS100_BACKLOG_A2  = table2array(SIM_2hop_RIS100_BACKLOG);
SNC_2hop_RIS100_BACKLOG = readtable('..\case150x150_power30x33\SNC\2hop\RIS100\BACKLOG.xlsx', 'NumHeaderLines',1);
SNC_2hop_RIS100_BACKLOG_A2  = table2array(SNC_2hop_RIS100_BACKLOG);






