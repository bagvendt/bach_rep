clear all;
close all;

TP = [47 38 40 46 59 42 26 22 23 19 25 27];
FP = [23 11 29 25 32 14 29 14 9 10 13 13];
FN = [18 27 25 19 6 23 2 6 5 9 3 1];

TP_2 = [51 51 61 28 23 28];
FP_2 = [26 36 42 31 14 20];
FN_2 = [14 14 4 0 5 0];

TP_3 = [60 61 28 28];
FP_3 = [40 61 37 26];
FN_3 = [5 4 0 0];

TP_4 = [62 28];
FP_4 = [52 39];
FN_4 = [3 0];

TP_5 = [62 28];
FP_5 = [53 41];
FN_5 = [3 0];

TP_6 = [63 28];
FP_6 = [55 43];
FN_6 = [2 0];

RECALL = TP./(TP+FN);
PRECISION = TP./(TP+FP);

RECALL_2 = TP_2./(TP_2+FN_2);
PRECISION_2 = TP_2./(TP_2+FP_2);

RECALL_3 = TP_3./(TP_3+FN_3);
PRECISION_3 = TP_3./(TP_3+FP_3);

RECALL_4 = TP_4./(TP_4+FN_4);
PRECISION_4 = TP_4./(TP_4+FP_4);

RECALL_5 = TP_5./(TP_5+FN_5);
PRECISION_5 = TP_5./(TP_5+FP_5);

RECALL_6 = TP_6./(TP_6+FN_6);
PRECISION_6 = TP_6./(TP_6+FP_6);

figure();
plot(1-PRECISION,RECALL,'or',1-PRECISION_2,RECALL_2,'ob',1-PRECISION_3,RECALL_3,'og',1-PRECISION_4,RECALL_4,'oc',1-PRECISION_5,RECALL_5,'om',1-PRECISION_6,RECALL_6,'ok');
% 1 = r?d, 2 = bl?, 3 = gr?n, 4 = cyan, 5 = magenta, 6 = sort
axis([0 1.1 0 1.1]);
set(gca,'fontsize',14);
xlabel('1-Precision');
ylabel('Recall');
title('Results: Recall - Precision');