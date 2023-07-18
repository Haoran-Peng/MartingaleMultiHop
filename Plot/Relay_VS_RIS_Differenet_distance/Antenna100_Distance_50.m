
index = zeros(1,4000);

for i = 1:4000
    index(i) = round(i*32/1000,2);
end

MarkerIndices = 1:10:length(index);

for i = 1:50:2001
    boxplot(SIM_2hop_RIS100_BACKLOG_A3(:,i).', 'position', index(i), 'labels', index(i), 'colors','r','widths', 2)
    hold on
    boxplot(SIM_2hop_DF100_BACKLOG_A3(:,i).', 'position', index(i), 'labels', index(i), 'colors','b','widths', 2)
    hold on
    boxplot(SIM_2hop_RIS100_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','m','widths', 2)
    hold on
    boxplot(SIM_2hop_DF100_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','k','widths', 2)
    hold on
end

plot(index, MT_2hop_RIS100_BACKLOG_A3,'Color','r','LineWidth',2);
hold on 

plot(index, MT_2hop_DF100_BACKLOG_A3, '--','Color','b','LineWidth',2);
hold on

plot(index, MT_2hop_RIS100_BACKLOG_A1,'-^','Color','m','LineWidth',2,'MarkerIndices',MarkerIndices);
hold on 

plot(index, MT_2hop_DF100_BACKLOG_A1,'--^', 'Color','k','LineWidth',2,'MarkerIndices',MarkerIndices);
hold on 

ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 10],'FontName', 'Times New Roman','FontSize',40)
ylim([10^(-3) 10^0]);
xlabel('Backlog (kB)', 'FontName', 'Times New Roman')
ylabel('Probability', 'FontName', 'Times New Roman')
legend({'RIS, 50m','DF relay, 50m','RIS, 150m','DF relay, 150m'},'Location','northeast', 'FontName', 'Times New Roman')
saveas(gcf,'png/Antenna100_Distance_150.png')
saveas(gcf,'fig/Antenna100_Distance_150.fig')
