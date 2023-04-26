#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:16:51 2023

@author: giuliosaibene
"""
### Right hand side of ODE GLOF system

import numpy as np
from V_P import V_P
from q_s import q_s
from dVsdt_func import Vs_dot
from Q_IN import Q_IN
from Q_IN_multiyear import Q_IN_multiyear
#%% GLOF ODEs

def glof_odes(t, x, param):

    # assign each ODE to a vector element
    S = x[0]
    N = x[1]
    V_s = x[2]
    
    #define inside functions
    
    psi = param.PSI_0 - N/param.L
    
    q = param.C_3*(S**param.ALPHA)*psi*(abs(psi)**(-0.5))
    
    #switch for subglacial component
    if param.use_Vs:
        dVsdt = Vs_dot(t, N, V_s, param) #from model fit
    else:
        dVsdt = 0
    
    #switch for variable meltwater supply
    if param.use_qin:
        q_in = Q_IN(t,param) #from Dave's data
    elif param.use_qin_multi:
        q_in = Q_IN_multiyear(t, param) #from synthetic multi-annual time series
    else:
        q_in = param.Q_IN/(param.q_inter_correction*param.q_melt_correction)
    
    #switch for effective pressure constraints 
    if param.bounds:
        q_tilda = q_s(N, q, q_in-dVsdt ,param)
    else:
        q_tilda = q
    
    #switch for variable V_p factor based on bathymetry
    if param.use_Vp:
        V_p = V_P(N, param)
    else:
        V_p = param.V_P_const
    
    v_0 = param.U_B_H_R*(1-(S/param.S_0))
    v_c = param.C_2*S*(abs(N)**(param.n-1))*N
    
    # define each ODE
    dSdt = param.C_1*q*psi + v_0 - v_c
    
    dNdt = (-1/V_p)*(q_in - q_tilda - dVsdt)
    
    return np.array([dSdt, dNdt, dVsdt])


