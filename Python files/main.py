# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:50:38 2015

@author: Mathew
"""

import clean_data as CD
import generate_portfolio as PF;


#create tables from google finance data

f = "training directory";
CD.CLEAN(f);

f = "testing directory";

CD.CLEAN(f, 'testing');

