function [ X ] = getPortfolio( index )

parent_dir = 'training directory';
pdfportfolio1 = strcat(parent_dir,'aapl.csv'); 
aapl = csvread(pdfportfolio1, 1,1); 
pdfportfolio2 = strcat(parent_dir,'dia.csv'); 
dia = csvread(pdfportfolio2, 1,1); 
pdfportfolio3 = strcat(parent_dir,'dis.csv'); 
dis = csvread(pdfportfolio3, 1,1); 
pdfportfolio4 = strcat(parent_dir,'f.csv'); 
f = csvread(pdfportfolio4, 1,1); 
pdfportfolio5 = strcat(parent_dir,'googl.csv'); 
googl = csvread(pdfportfolio5, 1,1); 
pdfportfolio6 = strcat(parent_dir,'ibm.csv'); 
ibm = csvread(pdfportfolio6, 1,1); 
pdfportfolio7 = strcat(parent_dir,'ko.csv'); 
ko = csvread(pdfportfolio7, 1,1); 
pdfportfolio8 = strcat(parent_dir,'nyt.csv'); 
nyt = csvread(pdfportfolio8, 1,1); 
pdfportfolio9 = strcat(parent_dir,'sso.csv'); 
sso = csvread(pdfportfolio9, 1,1); 
pdfportfolio10 = strcat(parent_dir,'ssys.csv'); 
ssys = csvread(pdfportfolio10, 1,1); 
pdfportfolio11 = strcat(parent_dir,'tm.csv'); 
tm = csvread(pdfportfolio11, 1,1); 
pdfportfolio12 = strcat(parent_dir,'tri.csv'); 
tri = csvread(pdfportfolio12, 1,1); 
pdfportfolio13 = strcat(parent_dir,'vz.csv'); 
vz = csvread(pdfportfolio13, 1,1); 

end

