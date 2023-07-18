
index = zeros(1,4000);

for i = 1:4000
    index(i) = round(i*32/1000,2);
end

for i = 1:50:2001
    boxplot(SIM_2hop_RIS25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','r','widths', 1)
    hold on
    boxplot(SIM_2hop_RIS100_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','b','widths', 1)
    hold on
    boxplot(SIM_2hop_RIS25_BACKLOG_A2(:,i).', 'position', index(i), 'labels', index(i), 'colors','c','widths', 1)
    hold on
    boxplot(SIM_2hop_RIS100_BACKLOG_A2(:,i).', 'position', index(i), 'labels', index(i), 'colors','k','widths', 1)
    hold on
end

MarkerIndices = 1:10:length(index);

plot(index, MT_2hop_RIS25_BACKLOG_A1,'Color','r','LineWidth',2);
hold on 

plot(index, MT_2hop_RIS100_BACKLOG_A1, '--','Color','b','LineWidth',2);
hold on 

plot(index, MT_2hop_RIS25_BACKLOG_A2,'-^','Color','m','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 

plot(index, MT_2hop_RIS100_BACKLOG_A2,'--^', 'Color','k','MarkerIndices',MarkerIndices,'LineWidth',2);
hold on 

ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 10],'FontName', 'Times New Roman','FontSize',40)
ylim([10^(-3) 10^0]);
xlabel('Backlog (kB)', 'FontName', 'Times New Roman')
ylabel('Probability', 'FontName', 'Times New Roman')
legend({'25 antennas, 20dBm/23dBm','100 antennas, 20dBm/23dBm','25 antennas, 30dBm/33dBm','100 antennas, 30dBm/33dBm'},'Location','northeast', 'FontName', 'Times New Roman')
saveas(gcf,'png\RIS_20x23.png')
saveas(gcf,'fig\RIS_20x23.fig')
