#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:56:44 2022

@author: giuliosaibene
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:32:22 2022

@author: giuliosaibene
"""

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from q_s import q_s

eps = np.finfo(float).eps

class param:
    C_1 = 1.3455e-9 # * m**3 / J
    C_2 = 3.44e-24 #  * Pa**-3 / s
    C_3 = 4.05e-2 # * m**(9/4) / Pa**0.5 * s*-1
    U_B_H_R = 3.12e-8 # * m**2 / s
    S_0 = 2e52 # * m**2
    S_IN = 55
    N_0 = 2e5 #* Pa
    PHI_0 = 178 # * Pa / m
    ALPHA = 5/4
    V_P = 4e6/9810 #4e6 * m**2/rho*g
    Q_IN = 10.9 #* m**3 / s# eventually also function of time
    N_MAX = 6e5 #* Pa
    L = 50e3 # * m
    K = 2 #(Kingslake et al 2015)
    T_m = 13
    n = 3
    rho = 1000
    g = 9.81
    t_days = 60*60*24
    bounds = True

t_start = 0
t_end = 1e8
t_step = 1000

t_span = np.array([t_start, t_end])
times = np.linspace(t_start,t_end,t_step)

x0 = np.array([param.S_IN,param.N_0])
 
#plt.plot(t_y,q_in)

def glof_odes(t, x, param):

    # assign each ODE to a vector element
    S = x[0]
    N = x[1]
    
    #define inside functions:
    
    phi = param.PHI_0 - N/param.L
    
    q = param.C_3*(S**param.ALPHA)*(abs(phi)**(-0.5))*phi
    
    if param.bounds:
        q = q_s(N,q,param)
    
    v_0 = param.U_B_H_R*(1-(S/param.S_0))
    v_c = param.C_2*S*(abs(N)**(param.n-1))*N
    
    # define each ODE
    dSdt = param.C_1*q*phi + v_0 - v_c
    dNdt = (-1/param.V_P)*(param.Q_IN - q) # WHERE TO CHANGE TO q_in

    return np.array([dSdt, dNdt])

#plotting on two separate plots

soln = solve_ivp(glof_odes, t_span, x0, args = (param,), rtol=1e-10, atol = 1e-10) 
 
t = (soln.t)/param.t_days
S = soln.y[0]
N = (soln.y[1])/(param.rho*param.g)

plt.subplot(2,1,1)
plt.plot(t, S, color="blue")
plt.ylabel("S (m$^2$)")
#plt.legend("S")

plt.subplot(2,1,2)
plt.plot(t, N, color = "red")
plt.ylabel("N (m)")
plt.xlabel("time (days)")
#plt.legend("N")

plt.tight_layout()

# =============================================================================
# plt.plot(S,N)
# plt.xlabel("S")
# plt.ylabel("N")
# =============================================================================

# =============================================================================
# # trying to call q_s and make into a list or array
# 
# q_s_v = np.vectorize(q_s)
# q_s_array = np.fromfunction(q_s_v(N, param.Q_IN, param), (1e9,1))
# 
# q_s_l = []
# for i in range(len(times)):
#     q_s_l.append(q_s(times[i], q, param)
#     
# print(q_s_l)
# plt.plot(t_q_s,q_s_l)
# =============================================================================

# Plotting N vs Q_in

# =============================================================================
# N_MAX = max(N)
# N_MIN = min(N)
# 
# q_in_var = np.linspace(1, 1000)
# =============================================================================
