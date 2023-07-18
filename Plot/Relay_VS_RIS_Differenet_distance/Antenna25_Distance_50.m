
index = zeros(1,4000);

for i = 1:4000
    index(i) = round(i*32/1000,2);
end

MarkerIndices = 1:10:length(index);

for i = 1:50:2001
    boxplot(SIM_2hop_RIS25_BACKLOG_A3(:,i).', 'position', index(i), 'labels', index(i), 'colors','r','widths', 2)
    hold on
    boxplot(SIM_2hop_DF25_BACKLOG_A3(:,i).', 'position', index(i), 'labels', index(i), 'colors','b','widths', 2)
    hold on
    boxplot(SIM_2hop_RIS25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','m','widths', 2)
    hold on
    boxplot(SIM_2hop_DF25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','k','widths', 2)
    hold on
end

plot(index, MT_2hop_RIS25_BACKLOG_A3,'Color','r');
hold on 

plot(index, MT_2hop_DF25_BACKLOG_A3, '--','Color','b');
hold on 

plot(index, MT_2hop_RIS25_BACKLOG_A1,'-^','Color','m','MarkerIndices',MarkerIndices);
hold on 

plot(index, MT_2hop_DF25_BACKLOG_A1,'--^', 'Color','k','MarkerIndices',MarkerIndices);
hold on 

ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 10],'FontName', 'Times New Roman','FontSize',40)

ylim([10^(-3) 10^0]);
xlabel('Backlog (kB)', 'FontName', 'Times New Roman')
ylabel('Probability', 'FontName', 'Times New Roman')
legend({'RIS, 50m','DF relay, 50m','RIS, 150m','DF relay, 150m'},'Location','northeast', 'FontName', 'Times New Roman')
saveas(gcf,'png/Antenna25_Distance_50.png')
saveas(gcf,'fig/Antenna25_Distance_50.fig')
