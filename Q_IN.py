#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:13:18 2023

@author: giuliosaibene
"""

import numpy as np

def Q_IN(t, param):
    t_original = param.serialtime17
    y_original = param.q_in_tot
    correction = param.q_inter_correction*param.q_melt_correction
    
    Q_IN = (np.interp(t, t_original, y_original))/correction
    
    return Q_IN