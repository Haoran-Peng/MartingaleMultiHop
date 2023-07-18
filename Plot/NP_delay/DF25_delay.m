time_slot_1_DF25 = 0.0123156;

time_slot_1_DF25_index = zeros(1,4000);

for i = 1:4000
    time_slot_1_DF25_index(i) = round(i*time_slot_1_DF25,3);
end


for i = 1:25:1001
    boxplot(SIM_1hop_DF25_URLLC_FIFO_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','c','widths', 2)
    hold on
    boxplot(SIM_1hop_DF25_EMBB_FIFO_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','b','widths', 2)
    hold on
    boxplot(SIM_2hop_DF25_URLLC_FIFO_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','r','widths', 2)
    hold on
    boxplot(SIM_2hop_DF25_EMBB_FIFO_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','k','widths', 2)
    hold on
end

MarkerIndices = 1:10:length(time_slot_1_DF25_index);

plot(time_slot_1_DF25_index, MT_1hop_DF25_URLLC_FIFO_A1,'-*','Color','c','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, SNC_1hop_DF25_URLLC_FIFO_A1, '--*','Color','c','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, MT_1hop_DF25_EMBB_FIFO_A1,'-o','Color','b','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, SNC_1hop_DF25_EMBB_FIFO_A1, '--o','Color','b','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, MT_2hop_DF25_URLLC_FIFO_A1,'-^','Color','r','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, SNC_2hop_DF25_URLLC_FIFO_A1,  '--^','Color','r','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, MT_2hop_DF25_EMBB_FIFO_A1,'Color','k','LineWidth',2);
hold on 
plot(time_slot_1_DF25_index, SNC_2hop_DF25_EMBB_FIFO_A1,  '--','Color','k','LineWidth',2);
hold on 


ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 5],'FontName', 'Times New Roman','FontSize',40)
ylim([10^(-3) 10^0]);
xlabel('Delay (ms)', 'FontName', 'Times New Roman')
ylabel('Probability', 'FontName', 'Times New Roman')
legend({'1-hop Martingale Curve, URLLC','1-hop SNC Curve, URLLC','1-hop Martingale Curve, eMBB','1-hop SNC Curve, eMBB','2-hop Martingale Curve, URLLC','2-hop SNC Curve, URLLC','2-hop Martingale Curve, eMBB','2-hop SNC Curve, eMBB'},'Location','northeast', 'FontName', 'Times New Roman')
saveas(gcf,'png\DF25.png')
saveas(gcf,'figure\DF25.fig')