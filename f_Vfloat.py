#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 15:13:13 2023

@author: giuliosaibene
"""

# effective pressure as a function of equilibrium floatation subglacial volume to be 
# used in dVsdt_func

import numpy as np

def f_Vfloat(V_S_float, param):
    return param.rho*param.g*(param.zwfloat - g_Vfloat(V_S_float, param))

def g_Vfloat(V_S_float, param):
    return param.k_1*np.log(np.sqrt(V_S_float**2+param.E**2))+param.k_2