function [ entropy ] = getEntropy()

entropy = zeros(13,1);
pdfportfolio1 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_aapl.csv'; 
aapl = csvread(pdfportfolio1, 1,0); 
pdfportfolio2 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_dia.csv'; 
dia = csvread(pdfportfolio2, 1,0); 
pdfportfolio3 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_dis.csv'; 
dis = csvread(pdfportfolio3, 1,0); 
pdfportfolio4 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_f.csv'; 
f = csvread(pdfportfolio4, 1,0); 
pdfportfolio5 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_googl.csv'; 
googl = csvread(pdfportfolio5, 1,0); 
pdfportfolio6 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_ibm.csv'; 
ibm = csvread(pdfportfolio6, 1,0); 
pdfportfolio7 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_ko.csv'; 
ko = csvread(pdfportfolio7, 1,0); 
pdfportfolio8 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_nyt.csv'; 
nyt = csvread(pdfportfolio8, 1,0); 
pdfportfolio9 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_sso.csv'; 
sso = csvread(pdfportfolio9, 1,0); 
pdfportfolio10 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_ssys.csv'; 
ssys = csvread(pdfportfolio10, 1,0); 
pdfportfolio11 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_tm.csv'; 
tm = csvread(pdfportfolio11, 1,0); 
pdfportfolio12 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_tri.csv'; 
tri = csvread(pdfportfolio12, 1,0); 
pdfportfolio13 = 'C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training\_PDF_BIN_1_training_TABLE_vz.csv'; 
vz = csvread(pdfportfolio13, 1,0); 

p1 = aapl(:,2)/sum(aapl(:,2));
h1 = -log(p1);
entropy(1,1) = p1' * h1;

p2 = dia(:,2)/sum(dia(:,2));
h2 = -log(p2);
entropy(2,1) = p2' * h2;

p3 = dis(:,2)/sum(dis(:,2));
h3 = -log(p3);
entropy(3,1) = p3' * h3;

p1 = f(:,2)/sum(f(:,2));
h1 = -log(p1);
entropy(4,1) = p1' * h1;

p1 = googl(:,2)/sum(googl(:,2));
h1 = -log(p1);
entropy(5,1) = p1' * h1;

p1 = ibm(:,2)/sum(ibm(:,2));
h1 = -log(p1);
entropy(6,1) = p1' * h1;

p1 = ko(:,2)/sum(ko(:,2));
h1 = -log(p1);
entropy(7,1) = p1' * h1;

p1 = nyt(:,2)/sum(nyt(:,2));
h1 = -log(p1);
entropy(8,1) = p1' * h1;

p1 = sso(:,2)/sum(sso(:,2));
h1 = -log(p1);
entropy(9,1) = p1' * h1;

p1 = ssys(:,2)/sum(ssys(:,2));
h1 = -log(p1);
entropy(10,1) = p1' * h1;

p1 = tm(:,2)/sum(tm(:,2));
h1 = -log(p1);
entropy(11,1) = p1' * h1;

p1 = tri(:,2)/sum(tri(:,2));
h1 = -log(p1);
entropy(12,1) = p1' * h1;

p1 = vz(:,2)/sum(vz(:,2));
h1 = -log(p1);
entropy(13,1) = p1' * h1;


end

