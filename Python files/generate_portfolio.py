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
    PARENT_DIRECTORY = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\";
    TABLE_DIRECTORY = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\tables.txt";
    PORTFOLIO_PATH = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\portfolio.csv";
    PORTFOLIO_PRICE_PATH = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\averageprice.csv";
    
    
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
    
    
    
PARENT_DIRECTORY = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\";
TABLE_DIRECTORY = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\tables.txt";
PORTFOLIO_PATH = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\portfolio.csv";
PORTFOLIO_PRICE_PATH = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\averageprice.csv";
TRAINING_DIRECTORY = r"C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\testing\\";
tt = r"C:\Users\Public\Documents\Stephy files\NJIT\Fall 2015\Project\training"

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