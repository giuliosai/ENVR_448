#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:52:30 2023

@author: giuliosaibene
"""
import numpy as np

#summation of gaussian model for meltwater over multiple n_years
def Q_IN_multiyear(t, param):
    def gaussian_multi(param, t, i):
        return (param.V_in_max_multi[i]/((param.q_inter_correction*param.q_melt_correction)*
                (param.Tmid_i*np.sqrt(2*np.pi))))*np.exp(-((t - param.t_i_multi[i])**2)/
                (2*(param.Tmid_i**2)))
    
    Q_IN_sum = sum(gaussian_multi(param, t, i) for i in range(param.n_years)) #summing over n_years
    return Q_IN_sum
