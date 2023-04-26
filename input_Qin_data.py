#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:36:57 2023

@author: giuliosaibene
"""

import pandas as pd
import numpy as np

def input_Qin_data(csv_path, date_to_serialtime):
    #where csv_path is the path to the file location of the meltwater data
    lakemelt = pd.read_csv(csv_path, parse_dates=['dates'], dayfirst = True, 
                           index_col = "dates")
    
    #bounding to period where data collection occurs
    lakemelt2 = lakemelt["2017-06-04 1:00:00":"2017-09-04 19:00:00"]

    #data given is in m^3 / 3 hours
    ablation = lakemelt2["abl"]
    rain = lakemelt2["rn"]
    ablation_kwl = lakemelt2["abl_kwl"]
    rain_kwl = lakemelt2['rn_kwl']
    
    lakemelt2 = lakemelt2.reset_index()
    dates = lakemelt2["dates"]
    time_q = pd.to_datetime(dates, format='%Y-%m-%d %H:%M:%S')
    serialtime_q = np.array(date_to_serialtime(time_q))
    t_days_dataq = (serialtime_q/(60*60*24)-(17321))

    q_in_tot = (np.array(ablation + rain + ablation_kwl + rain_kwl))/(60*60*3)
    #in m3 per second, data is originally provided in m3 per 3 hours

    return serialtime_q, t_days_dataq, q_in_tot
