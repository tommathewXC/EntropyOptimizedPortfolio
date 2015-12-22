# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:50:38 2015

@author: Mathew
"""

import clean_data as CD
import generate_portfolio as PF;
import subprocess;

PDF_GENERATOR_PATH = "path to cleaner exe"


def generatProbabilities():
    proc = subprocess.Popen(PDF_GENERATOR_PATH, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout;


#create tables from google finance data
CD.CLEAN();

