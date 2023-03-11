#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:13:13 2023

@author: giuliosaibene
"""

import numpy as np

# =============================================================================
# def Vs_dot_tilda(V_S_float, r, param):
#     return np.select([V_S_float > 0, V_S_float <= 0], 
#                      [Vs_dot(r, param),
#                       max(Vs_dot(r, param),0)])
# =============================================================================

def Vs_dot_tilda(N, V_S_float, param):
    return np.select([V_S_float > 0, V_S_float <= 0], 
                     [Vs_dot(N, V_S_float, param), max(Vs_dot(N, V_S_float, param),0)])

def Vs_dot(N, V_S_float, param):
    return -param.C_4*(V_S_float+param.V_S_float_0)**param.a_beam*(abs(N-f_Vfloat(V_S_float, param))**(param.n-1))*(N-f_Vfloat(V_S_float, param))

def f_Vfloat(V_S_float, param):
    return param.rho*param.g*(param.zwfloat - g_Vfloat(V_S_float, param))

def g_Vfloat(V_S_float, param):
    return V_S_float
    #return param.k_1*np.log(np.sqrt(V_S_float**2+param.E**2))+param.k_2