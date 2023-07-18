time_slot_1_MIMO = 0.02237456;
time_slot_1_DF25 = 0.0123156;
time_slot_1_DF100 = 0.00901951;
time_slot_1_RIS25 = 0.01924043;
time_slot_1_RIS100 = 0.01469898;

time_slot_2_MIMO = 0.01173887;
time_slot_2_DF25 = 0.00838662;
time_slot_2_DF100 = 0.00758194;
time_slot_2_RIS25 = 0.01075383;
time_slot_2_RIS100 = 0.00911949;

time_slot_1_MIMO_index = zeros(1,4000);
time_slot_1_DF25_index = zeros(1,4000);
time_slot_1_DF100_index = zeros(1,4000);
time_slot_1_RIS25_index = zeros(1,4000);
time_slot_1_RIS100_index = zeros(1,4000);

time_slot_2_MIMO_index = zeros(1,4000);
time_slot_2_DF25_index = zeros(1,4000);
time_slot_2_DF100_index = zeros(1,4000);
time_slot_2_RIS25_index = zeros(1,4000);
time_slot_2_RIS100_index = zeros(1,4000);

for i = 1:4000
    time_slot_1_MIMO_index(i) = round(i*time_slot_1_MIMO,3);
    time_slot_1_DF25_index(i) = round(i*time_slot_1_DF25,3);
    time_slot_1_DF100_index(i) = round(i*time_slot_1_DF100,3);
    time_slot_1_RIS25_index(i) = round(i*time_slot_1_RIS25,3);
    time_slot_1_RIS100_index(i) = round(i*time_slot_1_RIS100,3);
    time_slot_2_MIMO_index(i) = round(i*time_slot_2_MIMO,3);
    time_slot_2_DF25_index(i) = round(i*time_slot_2_DF25,3);
    time_slot_2_DF100_index(i) = round(i*time_slot_2_DF100,3);
    time_slot_2_RIS25_index(i) = round(i*time_slot_2_RIS25,3);
    time_slot_2_RIS100_index(i) = round(i*time_slot_2_RIS100,3);
end

% for i = 1:20:551
%     boxplot(SIM_2hop_RIS25_URLLC_FIFO_A1(:,i).', 'position', time_slot_1_RIS25_index(i), 'labels', time_slot_1_RIS25_index(i), 'colors','r','widths', 1)
%     hold on
%     boxplot(SIM_2hop_RIS25_URLLC_SP_A1(:,i).', 'position', time_slot_1_RIS25_index(i), 'labels', time_slot_1_RIS25_index(i), 'colors','b','widths', 1)
%     hold on   
%     boxplot(SIM_2hop_RIS25_URLLC_EDF_A1(:,i).', 'position', time_slot_1_RIS25_index(i), 'labels', time_slot_1_RIS25_index(i), 'colors','g','widths', 1)
%     hold on
% end
% plot(time_slot_1_RIS25_index, MT_2hop_RIS25_URLLC_FIFO_A1,'Color','r');
% hold on 
% plot(time_slot_1_RIS25_index, MT_2hop_RIS25_URLLC_SP_A1,'Color','b');
% hold on 
% plot(time_slot_1_RIS25_index, MT_2hop_RIS25_URLLC_EDF_A1,'Color','g');
% hold on 

for i = 1:20:551
    boxplot(SIM_2hop_DF25_URLLC_FIFO_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','b','widths', 1)
    hold on
    boxplot(SIM_2hop_DF25_URLLC_SP_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','r','widths', 2)
    hold on   
    boxplot(SIM_2hop_DF25_URLLC_EDF_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','k','widths', 1)
    hold on
end
plot(time_slot_1_DF25_index, MT_2hop_DF25_URLLC_FIFO_A1,':','Color','b','LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, MT_2hop_DF25_URLLC_SP_A1,'Color','r','LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, MT_2hop_DF25_URLLC_EDF_A1,'--','Color','k');
hold on


ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 2],'FontName', 'Times New Roman','FontSize',40)

ylim([10^(-3) 10^0]);
xlabel('Delay (ms)', 'FontName', 'Times New Roman')
ylabel('Probability', 'FontName', 'Times New Roman')
legend({'Non-preemption','Static priority','EDF'},'Location','northeast', 'FontName', 'Times New Roman')
saveas(gcf,'png\DF25_URLLC.png')
saveas(gcf,'fig\DF25_URLLC.fig')

