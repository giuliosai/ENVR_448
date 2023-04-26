#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:10:13 2022

@author: giuliosaibene
"""

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

#solver of glof ODE system

from scipy.integrate import solve_ivp
from glof_odes import glof_odes
import os
os.chdir("/Users/giuliosaibene/Desktop/University/UBC/Y4/Directed Studies")

#%% 

def glof_solver(param):
    
    # takes the RHS of the ODE equation to solve ("glof_odes"),
    # the span of time values to evaluate the solution over ("t_span")
    # the initial S and N values ("param.x0")
    soln = solve_ivp(glof_odes, param.t_span_ext, param.x0, 
                     args = (param,), rtol = param.rtol, atol = param.atol)
    
    soln.param = param #appends parameters used to soln class
    
    return soln
    



