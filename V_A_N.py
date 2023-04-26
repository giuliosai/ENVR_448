#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:03:38 2023

@author: giuliosaibene
"""

#empirical relationship between N and subaerial volume (V_A)

import numpy as np

def V_A_N(N, param):
    return param.k_3*np.exp(param.k_4*(param.zwfloat - N/(param.rho*param.g)))


