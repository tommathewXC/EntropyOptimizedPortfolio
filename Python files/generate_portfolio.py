# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:22:04 2015

@author: Mathew
"""

import pandas as P;
import numpy;
import csv




def getRateFromVector(vector):
    if isinstance(vector, P.core.series.Series):
        rate = [];
        previous = 0;
        for i in range(len(vector)):
            if i == 0:
                rate.append(0);
            else:
                if previous != 0:
                    rate.append((vector[i] - previous)/(previous));
                else:
                    rate.append(0);
                    
                previous = vector[i];
        return rate;
        
        
        
def generatePortfolioAndPriceTables():
    PARENT_DIRECTORY = r"PARENT_DIRECTORY";
    TABLE_DIRECTORY = r"TABLE_DIRECTORY";
    PORTFOLIO_PATH = r"PORTFOLIO_PATH";
    PORTFOLIO_PRICE_PATH = r"PORTFOLIO_PRICE_PATH";
    
    
    TABLES = [];   
    tabs = []
    prices = [];
    xnames = [];  
    with open(TABLE_DIRECTORY, "r") as F:
        for line in F:
            TABLES.append(line.replace("\n",""));
    xnames.append("Date");
    
    for x in range (len(TABLES)):
        a = P.read_csv(PARENT_DIRECTORY + TABLES[x]).sort(['Year','Month','Day']).reset_index();
        b = P.read_csv(PARENT_DIRECTORY + TABLES[x]).sort(['Year','Month','Day']).reset_index();
        stockname =  TABLES[x].replace("training_TABLE_","").replace(".csv",""); 
        rate = getRateFromVector(a.Average);   
        price = numpy.floor(b.Average);
        del a['index'];
        del a['Day'];
        del a['Month'];
        del a['Year'];
        del a['Volume'];
        del a['Average'];
        del b['index'];
        del b['Day'];
        del b['Month'];
        del b['Year'];
        del b['Volume'];
        del b['Average'];
        a[stockname] = P.core.series.Series(rate);
        b[stockname] = price;
        tabs.append(a);
        prices.append(b);
        xnames.append(stockname)
    
    v3 = tabs[0];
    for _X in range(1, len(tabs)):
        v = tabs[_X];
        v3 = v3.merge(v, on="Date");
    
    
    b2 = prices[0];
    
    for _Y in range(1, len(prices)):
        b1 = prices[_Y];
        b2 = b2.merge(b1, on = "Date")
            
    numpy.savetxt(PORTFOLIO_PATH, v3[xnames], fmt="%s", header = ",".join(xnames ) , delimiter = ",") 
    numpy.savetxt(PORTFOLIO_PRICE_PATH, b2[xnames], fmt="%s", header = ",".join( xnames ) , delimiter = ",") 
    print "Portfolio rates and average prices have been generated";
    
    
    
PARENT_DIRECTORY = r"parent directory";
TABLE_DIRECTORY = r"path to table text file";
PORTFOLIO_PATH = r"path to portfolio csv";
PORTFOLIO_PRICE_PATH = r"path to average price csv";
TRAINING_DIRECTORY = r"path to testing directory";
tt = r"path to training directory"

TABLES = [];   
tabs = []
prices = [];
xnames = [];  
with open(TABLE_DIRECTORY, "r") as F:
    for line in F:
        TABLES.append(line.replace("\n",""));
xnames.append("Date");    


c = open(TRAINING_DIRECTORY+'temp.txt','w');
for i in range(0, len(TABLES)):
    c.writelines('pdfportfolio'+str(i+1)+' = '+"'"+tt +TABLES[i].replace('training_TABLE_','\_PDF_BIN_1_training_TABLE_')+ "'"+'; \n')
    c.writelines(TABLES[i].replace('training_TABLE_','').replace('.csv','') +' = csvread(pdfportfolio'+str(i+1)+', 1,0); \n');
c.close();