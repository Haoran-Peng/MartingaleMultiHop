time_slot_1_MIMO = 0.02237456;
time_slot_1_DF25 = 0.0123156;
time_slot_1_DF100 = 0.00901951;
time_slot_1_RIS25 = 0.01924043;
time_slot_1_RIS100 = 0.01469898;

time_slot_1_MIMO_index = zeros(1,4000);
time_slot_1_DF25_index = zeros(1,4000);
time_slot_1_DF100_index = zeros(1,4000);
time_slot_1_RIS25_index = zeros(1,4000);
time_slot_1_RIS100_index = zeros(1,4000);

for i = 1:4000
    time_slot_1_MIMO_index(i) = round(i*time_slot_1_MIMO,3);
    time_slot_1_DF25_index(i) = round(i*time_slot_1_DF25,3);
    time_slot_1_DF100_index(i) = round(i*time_slot_1_DF100,3);
    time_slot_1_RIS25_index(i) = round(i*time_slot_1_RIS25,3);
    time_slot_1_RIS100_index(i) = round(i*time_slot_1_RIS100,3);
end

for i = 1:20:551
    boxplot(SIM_2hop_DF25_URLLC_SP_A1(:,i).', 'position', time_slot_1_DF25_index(i), 'labels', time_slot_1_DF25_index(i), 'colors','b','widths', 1)
    hold on   
    boxplot(SIM_2hop_RIS25_URLLC_SP_A1(:,i).', 'position', time_slot_1_RIS25_index(i), 'labels', time_slot_1_RIS25_index(i), 'colors','r','widths', 1)
    hold on
end
plot(time_slot_1_DF25_index, MT_2hop_DF25_URLLC_SP_A1,'Color','b');
hold on 
plot(time_slot_1_RIS25_index, MT_2hop_RIS25_URLLC_SP_A1,'Color','r');
hold on 

ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 5])

ylim([10^(-3) 10^0]);
xlabel('delay (ms)')
ylabel('probability')

legend({'DF25\_URLLC','RIS25\_URLLC'},'Location','northeast')

saveas(gcf,'fig/antenna25_URLLC.fig')
saveas(gcf,'png/antenna25_URLLC.png')


