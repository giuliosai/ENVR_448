# ENVR_448
Directed studies code

#READ ME

V1.npy —> V1: N model output, with Vs and q_in variable turned off

V2: When with V_p turned on constrained model was working, changed c2, c3, u_b_h_r, from April 18 2023

V3: Optimised c2 and u_b_h_r with Vp on, Vs off, q_in variable off, April 19 2023, before changing c3 and ALPHA

V4: Optimised c3 and ALPHA for as of April 19 2023 best fit so far of GLOF with secondary flood seen

V5: Optimised c3 and ALPHA after having turned on the time series of q_in and and created best fit, April 20, 2023

V6: Optimised parameters used for outputting reasonable results with variable q_in and Vs both turned on, April 20, 2023
- param_V6.pickle got overwritten accidentally

PART 2: Multi-year analysis of secondary floods with periodic meltwater input

atol kept at 1000 for all of these, except for a few

Multi1: V_in_max = 0.7* 4.75e7 m^3 (from data), only one considerable secondary flood (Vs = On)
Multi2: V_in_max = *0.8 factor, no considerable secondary flood (Vs = On)
Multi3: V_in_max = *1 factor, no secondary drainage at all (Vs = On)
Multi4: V_in_max = *1.3 factor, alternating sharp secondary floods of large amplitude  (Vs = On)
Multi5: V_in_max = *1.5 factor, secondary floods all become more similar, but decrease in amplitude, first flood reaches maximum lake volume possible (Vs = On)
Multi6: V_in_max = *2.5 factor, double secondary floods appear, as well for Vs (Vs = On)
Multi7: V_in_max = *2.8 factor, consistent double secondary floods and some small double secondary floods in Vs too (Vs = On)
Multi8: V_in_max = *0.7 (Vs = Off), 
Multi9: V_in_max = *0.8 (Vs = Off)
Multi10: V_in_max = *1 (Vs = Off)
Multi11: V_in_max = *1.3 (Vs = Off)
Multi12: V_in_max = *1.5 (Vs = Off)
Multi13: V_in_max = *2.5 (Vs = Off), had to increase atol to 2000
Multi14: V_in_max = *2.8 (Vs = Off), had to increase atol to 2500
