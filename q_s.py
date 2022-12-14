#!/usr/bin/env python
# coding: utf-8

# In[1]:

# In[2]:
import numpy as np

def q_s(N, q, param): # WHERE TO ADD q_in as another variable
         #N = np.asarray(N)
         #q_s = np.zeros(N.shape)
     if (N <= 0).any():
         return q_s == max(q, param.Q_IN) # where to change Q_IN
     elif (N > 0).any() and (N < param.N_MAX).any():
         return q_s == q
     elif (N >= param.N_MAX).any():
         return q_s == min(q, param.Q_IN) # where to change Q_IN

# =============================================================================
# def q_s(N, q, param):
#     np.piecewise([N,q,param],[N <= 0, N > 0, N >= param.N_MAX], 
#                    [lambda N, q, param : max(q, param.MAX_Q_IN), q, 
#                     lambda N, q, param : min(q, param.MIN_Q_IN)])
#     
# =============================================================================
# =============================================================================
# def q_s(N, q, param):
#     np.select([N <= 0, N > 0, N >= param.N_MAX], 
#                    [lambda N, q, param : max(q, param.MAX_Q_IN), q, 
#                     lambda N, q, param : min(q, param.MIN_Q_IN)])
# 
# =============================================================================

# In[ ]:




