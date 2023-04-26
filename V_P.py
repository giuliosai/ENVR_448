#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:49:51 2023

@author: giuliosaibene
"""

import numpy as np

def V_P(N, param):
    return (param.k_3*param.k_4/(param.rho*param.g)) * np.exp(param.k_4*(param.zwfloat - N/(param.rho*param.g)))


