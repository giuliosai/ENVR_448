#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:11:23 2023

@author: giuliosaibene
"""

#quasi-physical model for the subglacial component of the model

from f_Vfloat import f_Vfloat

def Vs_dot(t, N, Vs, param):

    #N = np.interp(t, serialtime17, N_17) #interpolate N data onto time t
    f_V_s = f_Vfloat(Vs, param);#evaluate f(V_s) from the fit you have created
    
    N_f_Vs = N - f_V_s;
    
    dVsdt = -param.C_4 * (Vs + param.V_S_float_0)**param.a_beam * (abs(N_f_Vs))**(param.b_beam - 1) * (N_f_Vs)
    
    return dVsdt