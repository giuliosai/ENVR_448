#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:46:10 2023

@author: giuliosaibene
"""

import pandas as pd
import numpy as np

def input_waterbalance_data(csv_path, date_to_serialtime, param):
    
    #where csv_path is the local path to the file with the data
    df = pd.read_csv(csv_path, parse_dates=['dtime'], dayfirst=True, 
                     index_col = "dtime")
    
    #bounding based on data collection period
    df2 = df["2017-06-04 1:00:00":"2017-09-04 19:00:00"]

    h = df2["elevation"]
    V_A = df2["aer_vol"]
    V_S_float = df2["subvol_float"] #equilibrium V_S
    V_S_GPS = df2['subvol_gps'] #actual V_S data starts from 2017-06-23 1:00:00
    V_E = df2["engvol_gps"]
    V_tot = df2["tot_vol"]
    V_in = df2["input_vol"]
    
    df2 = df2.reset_index()
    time17 = df2["dtime"]
    time = pd.to_datetime(time17, format='%Y-%m-%d %H:%M:%S')
    serialtime17 = np.array(date_to_serialtime(time))
    t_days_data17 = (serialtime17/(60*60*24)-(17321))

    #calculating effective pressure from data water elevation
    N_17 = param.rho*param.g * (param.zwfloat - h)
    
    return serialtime17, t_days_data17, h, N_17, V_A, V_S_GPS, V_E, V_tot, V_in, V_S_float
