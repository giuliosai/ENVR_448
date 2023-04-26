#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:13:28 2023

@author: giuliosaibene
"""

import numpy as np
from input_waterbalance_data import input_waterbalance_data
from input_Qin_data import input_Qin_data
from serial_t_conversion import date_to_serialtime
    
class param:
    C_1 = 3e-9 #1.3455e-9  # * m**3 / J
    C_2 = 2.5e-23 #3.44e-24 #  * Pa**-3 / day #controls closure term
    C_3 = 0.07  #0.0524 # 4.05e-2 # * m**(9/4) / Pa**0.5 * day*-1, controls q out
    C_4 = 6e-18
    k_1 = 8.335721184131165 #for g_Vfloat fit
    k_2 = 1469.5012823278607 #for g_Vfloat fit
    k_3 = 6.861843102945029e-26 #for V_A(h) for V_p
    k_4 = 0.045968949164897015 #for V_A(h) for V_p
    E = 32344.597916174258 #added constant for g_Vfloat fit to prevent log(0)
    U_B_H_R = 6.6e-8 #3.12e-8 # * m**2 / day, controls opening term
    S_0 = 2e52 # * m**2
    PSI_0 = 178 # * Pa / m
    ALPHA = 1.95 #1.25
    a_beam = 1.39
    V_P_const= 30 #4e6 * m**2/rho*g
    Q_IN = 47529673.07/(4*(1500534000.0 - 1496538000.0)) #4.78*1 #* m**3 / s, 4.78 m^3 / s from mean of Dave's data 
    N_MAX = 9810*(1610.86-1557) #* Pa , based on h to N conversion using zwfloat when lake is dry
    L = 50e3 # * m
    K = 2 #(Kingslake et al 2015)
    T_m = 13
    n = 3
    b_beam = 1.66
    rho = 1000
    g = 9.81
    
    zwfloat = 1610.865 #defines water level at which floatation is reached
    t_days = 60*60*24
    t_days_in_year = 365
    bounds = True
    use_Vp = True #turns on variable V_p factor
    use_Vs = False #turns on subglacial component
    use_qin = False #turns on variable q_in from data
    use_qin_multi = True #turns on variable q_in from synthetic time series
    V_S_float_0 = 50*5000
    q_inter_correction = 1.1601441841694842 #to correct for interpolation error
    q_melt_correction = 2.7910874478773655 #to correct for melt model errors
    
    #initial values
    N_0 = 9810*(1610.86 - 1557) #* Pa 1575 m is first h observed, made to empty lake when t_span starts before June 4
    S_IN = U_B_H_R / (C_2*(N_0**n))
    V_S_in = 297993 #m^3 based on first V_S_float value
    x0 = np.array([S_IN, N_0, V_S_in])
    
    #parameters for gaussian modelled multi-year meltwater input
    n_years = 6
    V_in_max = 47529673.07 #m^3
    V_in_max_multi = [47529673.07*2.8]*n_years
    Tmid_i = 1500534000.0 - 1496538000.0 #half the length of melt season in serial time, corresponds to ~46 days after June 4 2017
    t_i = 1499990400 #serial time of peak melt, 40 days after June 4 2017
    t_i_multi = [1499990400 + i*(365*60*60*24) for i in range(n_years)]#for 40, 36, 46, and 34 days after June 4 2017 for 4 years series
    
    #solver tolerances
    rtol = 1e-7
    atol = 2500
    
    #tuning parameters
    N_star = 9810*(20)
    S_star = U_B_H_R / (C_2*(N_star**n))
    C_3f = C_3*S_star**(1.96-ALPHA)
    
#appending data to param

serialtime17, t_days_data17, h, N_17, V_A, V_S_GPS, V_E, V_tot, V_in, V_S_float = input_waterbalance_data(
        "waterbalance_discharge.csv", date_to_serialtime, param)

serialtime_q, t_days_dataq, q_in_tot = input_Qin_data("inputs.csv", date_to_serialtime)

param.serialtime17 = serialtime17
param.t_days_data17 = t_days_data17
param.h = h
param.N_17 = N_17
param.V_A = V_A
param.V_S_GPS = V_S_GPS
param.V_E = V_E
param.V_tot = V_tot
param.V_in = V_in
param.V_S_float = V_S_float

param.serialtime_q = serialtime_q
param.t_days_dataq = t_days_dataq
param.q_in_tot = q_in_tot

#defining integral range time period based on data
param.t_span = (param.serialtime17[0], param.serialtime17[-1] + 1.5*(serialtime17[-1] - serialtime17[-743]))
param.t_span_ext = (param.t_days*(-100)+17321*param.t_days, 
                              param.n_years*param.t_days*(365)+17321*param.t_days)

#exporting param class as .pickle file:  
# =============================================================================
# with open('params_multi7.pickle', 'wb') as f:
#     pickle.dump(param, f)
# =============================================================================

