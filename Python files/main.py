# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:50:38 2015

@author: Mathew
"""

import clean_data as CD
import generate_portfolio as PF;
import subprocess;

PDF_GENERATOR_PATH = "C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\FinanceOptimizer.exe"


def generatProbabilities():
    proc = subprocess.Popen(PDF_GENERATOR_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout;


#create tables from google finance data
CD.CLEAN();
interaction = True;
trigger_optimization = False;





while interaction:
    try:
        x = input("enter 1 to generate probabilities. Enter 0 to terminate \n" );
        if int(x) == 1:
            PF.generatePortfolioAndPriceTables();
            trigger_optimization = True;
        if int(x) == 0:
            PF.generatePortfolioAndPriceTables();
            interaction = False;
    except SyntaxError:
        print "Enter a valid character dawg ";
    except NameError:
        print "Enter a number dawg ";







if trigger_optimization:
    print "Optimization logic goes here";