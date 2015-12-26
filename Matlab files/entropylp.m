loadtestdata
 
M = [aapl(:,1)  dia(:,1) dis(:,1) f(:,1) googl(:,1) ibm(:,1) ko(:,1) nyt(:,1) sso(:,1) ssys(:,1) tm(:,1) tri(:,1) vz(:,1)];



[s1, x1, xm1] = entgen( 1000, M);
[s2, x2, xm2] = entgen( 1, M);
[s3, x3, xm3] = entgen( 0.028, M);


figure;
t1 = size(s1);
t1 = t1(1,1);
t1 = 1:t1;
t2 = size(s3);
t2 = t2(1,1);
t2 = 1:t2;
plot(t2, s2/xm2, 'red', t2, s3/xm3, 'black');

ylabel('Growth ratio');
xlabel('Months');
title('Growth of portfolio between 11/2011 and 12/2015');
legend('alpha = 1','alpha = 0.028','Location','northoutside','Orientation','vertical');
grid on;

t = 0:0.001:0.0500;
p = t;
k = 1;
for i = t
    p(1,k) = ENTROPORTFOLIO( i, M);
    k = k+1;
end

figure;
plot(t,p)
grid on;
ylabel('Average portfolio return after 50 months');
xlabel('Control parameter value');
title('Visualizing the risk-return tradeoff when measuring risk with entropy')



[s3, x3, xm3] = entgen( 0.038, M);


figure;
t1 = size(s3);
t1 = t1(1,1);
t1 = 1:t1;
plot(t1, s3/xm3, 'black');

ylabel('Growth ratio');
xlabel('Months');
title('Growth of portfolio between 11/2011 and 12/2015 at a good entropy bound');
legend('alpha = 0.038','Location','northoutside','Orientation','vertical');
grid on;


[s1, x1, xm1] = entgen( 0, M);% figure;
t1 = size(s1);
t1 = t1(1,1);
t1 = 1:t1;
plot(t1, s1/xm1, 'red');
ylabel('Growth ratio');
xlabel('Months starting October 2011');
title('Growth of portfolio between 11/2011 and 12/2015 no entropy restraint');
grid on;
x1