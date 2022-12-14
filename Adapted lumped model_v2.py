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
from numericalunits import m, s, Pa, J
from q_s import q_s

class param:
    C_1 = 1.3455e-9 # * m**3 / J
    C_2 = 3.44e-24 #  * Pa**-3 / s
    C_3 = 4.05e-2 #4.05e-2 * m**(9/4) / Pa**0.5 * s*-1
    U_B_H_R = 3.12e-8 # * m**2 / s
    S_0 = 300 #100000 * m**2
    N_0 = 3e5 #* Pa
    PHI_0 = 178 # * Pa / m
    ALPHA = 5/4
    V_P = 4000 #4e6 * m**2
    Q_IN = 15.5 #* m**3 / s# eventually also function of time
    N_MAX = 2e5 #* Pa
    L = 5000 # * m
    K = 2 #(Kingslake et al 2015)
    T_m = 13
    n = 3
    bounds = True

t_start = 0
t_end = 1e8
t_step = 1000

t_span = np.array([t_start, t_end])
times = np.linspace(t_start,t_end,t_step)

x0 = np.array([param.S_0,param.N_0])

### adaptation: making q_in a function of temperature  (not being used for now)
  
# t_y = np.linspace(0,365,365)
# T = param.T_m*np.sin(2*np.pi*(t_y-0.29)) #(Kingslake et al 2015)
    
# q_in = np.piecewise(T, [T > 0, T <= 0], [lambda T : T*param.K, 0])
 
#plt.plot(t_y,q_in)

def glof_odes(t, x, param):

    # assign each ODE to a vector element
    S = x[0]
    N = x[1]
    
    #define inside functions: would be helpful if I could do this globally

    phi = param.PHI_0 - N/param.L
    
    global q
    q = param.C_3*(S**param.ALPHA)*phi*(abs(phi)**(-0.5))
    
    if param.bounds:
        q = q_s(N,q,param)
    
    v_0 = param.U_B_H_R*(1-(S/param.S_0))
    v_c = param.C_2*S*(abs(N)**(param.n-1))*N
    
    # define each ODE
    dSdt = param.C_1*q*phi + v_0 - v_c #WHERE TO ADD q_in
    dNdt = (-1/param.V_P)*(param.Q_IN - q) # WHERE TO CHANGE TO q_in

    return np.array([dSdt, dNdt])

### 

# =============================================================================
# # trying to call q_s and make into a list
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

###

#plotting on two separate plots

soln = solve_ivp(glof_odes, t_span, x0, args = (param,), rtol=1e-10, atol = 1e-10) 
 
t = soln.t
S = soln.y[0]
N = soln.y[1]

plt.subplot(2,1,1)
plt.plot(t, S, color="blue")
plt.ylabel("S")
plt.xlabel("time")
#plt.legend("S")

plt.subplot(2,1,2)
plt.plot(t, N, color = "red")
plt.ylabel("N")
plt.xlabel("time")
#plt.legend("N")

plt.tight_layout()

# =============================================================================
# plt.plot(S,N)
# plt.xlabel("S")
# plt.ylabel("N")
# =============================================================================

