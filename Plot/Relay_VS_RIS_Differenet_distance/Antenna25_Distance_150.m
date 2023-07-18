
index = zeros(1,4000);

for i = 1:4000
    index(i) = round(i*32/1000,2);
end


for i = 1:50:2001
    boxplot(SIM_2hop_RIS25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','r','widths', 1)
    hold on
    boxplot(SIM_2hop_DF25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','b','widths', 1)
    hold on
end

plot(index, MT_2hop_RIS25_BACKLOG_A1,'Color','r');
hold on 

plot(index, MT_2hop_DF25_BACKLOG_A1, 'Color','b');
hold on 

ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 10])
ylim([10^(-3) 10^0]);
xlabel('backlog (kB)')
ylabel('probability')
% legend({'RIS100','DF100'},'Location','northeast')
legend({'RIS25','DF25'},'Location','northeast')
saveas(gcf,'png/Antenna25_Distance_150.png')
saveas(gcf,'fig/Antenna25_Distance_150.fig')
