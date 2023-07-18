index = zeros(1,4000);

for i = 1:4000
    index(i) = round(i*32/1000,2);
end
index1 = zeros(1,5555);
for i = 1:5555
    index1(i) = round(i*32/1000,2);
end

for i = 1:50:2001
    boxplot(SIM_1hop_DF25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','r','widths', 1)
    hold on
    boxplot(SIM_2hop_DF25_BACKLOG_A1(:,i).', 'position', index(i), 'labels', index(i), 'colors','b','widths', 1)
    hold on
end

MarkerIndices = 1:10:length(index);

M1=plot(index, MT_1hop_DF25_BACKLOG_A1,'-*','Color','r','MarkerIndices',MarkerIndices,'LineWidth',1);
hold on 
plot(index1, SNC_1hop_DF25_BACKLOG_A1, '--*','Color','r','MarkerIndices',MarkerIndices,'LineWidth',1);
hold on 
plot(index, MT_2hop_DF25_BACKLOG_A1,'Color','b','LineWidth',1);
hold on 
plot(index1, SNC_2hop_DF25_BACKLOG_A1, '--','Color','b','LineWidth',1);
hold on 


ax = gca; 
ax.YAxis.Scale ="log";
set(gca, 'XTickMode', 'auto', 'XTickLabelMode', 'auto','XLim',[0 10], 'FontName', 'Times New Roman','FontSize',40)
ylim([10^(-3) 10^0]);
xlabel('Backlog (kB)', 'FontName', 'Times New Roman')
ylabel('Probability', 'FontName', 'Times New Roman')
legend({'Single-hop Martingale Curve','Single-hop SNC Curve','Two-hop Martingale Curve','Two-hop SNC Curve'},'Location','northeast', 'FontName', 'Times New Roman')
saveas(gcf,'png\DF25.png')
saveas(gcf,'figure\DF25.fig')