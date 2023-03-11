#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:55:30 2023

@author: giuliosaibene
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colors
import numpy as np
import os
import scipy.optimize
from scipy.optimize import curve_fit
#from lmfit.models import PowerLawModel, LinearModel
from sklearn.metrics import r2_score
os.chdir("/Users/giuliosaibene/Desktop/University/UBC/Y4/Directed Studies")

#%% data pre-processing

df = pd.read_csv("waterbalance_discharge.csv", parse_dates=['dtime'], 
                 dayfirst = True)

df2 = df.dropna(subset = 'elevation', axis = 0)

V_A = df2["aer_vol"]
V_S_GPS = df2["subvol_gps"]
V_S_PC = df2["subvol_pc"]
V_S_float = df2["subvol_float"]
V_E_GPS = df2["engvol_gps"]
V_E_PC = df2['engvol_pc']
h = df2["elevation"]
V_I = df2['input_vol']
time = df2["dtime"]
V_T = V_A + V_S_GPS + V_E_GPS

# splitting data into filling and draining phase
# max_V_A = V_A.max()
df2['dtime'] = pd.to_datetime(df2['dtime'])
df2.set_index('dtime', inplace=True)
peak_V_A_time = "2017-08-17 19:00:00"
df3_filling = df2.loc[:peak_V_A_time,:]
h_filling = df3_filling['elevation']
V_A_filling = df3_filling['aer_vol']
V_S_GPS_filling = df3_filling['subvol_gps']
V_E_GPS_filling = df3_filling['engvol_gps']
V_I_filling = df3_filling['input_vol']
df3_filling = df3_filling.reset_index(drop=False)
time_filling = df3_filling.iloc[:,0]

df3_draining = df2.loc[peak_V_A_time:,:]
h_draining = df3_draining['elevation']
V_A_draining = df3_draining['aer_vol']
V_S_GPS_draining = df3_draining['subvol_gps']
V_E_GPS_draining = df3_draining['engvol_gps']
V_I_draining = df3_draining['input_vol']
df3_draining = df3_draining.reset_index(drop=False)
time_draining = df3_draining.iloc[:,0]
V_T_draining = V_A_draining + V_S_GPS_draining + V_E_GPS_draining

#selecting filling data past kink
V_A_incr_time = '2017-07-03 13:00:00'
df3_filling.set_index('dtime', inplace=True)
df4_filling = df3_filling.loc[V_A_incr_time:,:]
h_filling_cont = df4_filling['elevation']
V_A_filling_cont = df4_filling['aer_vol']
V_S_GPS_filling_cont = df4_filling['subvol_gps']
V_E_GPS_filling_cont = df4_filling['engvol_gps']
df4_filling = df4_filling.reset_index(drop=False)
time_filling_cont = df4_filling.iloc[:,0]
V_T_filling_cont = V_A_filling_cont + V_S_GPS_filling_cont + V_E_GPS_filling_cont

#selecting all data past kink
df2_fnc = df2.loc[V_A_incr_time:,:]
h_fnc = df2_fnc['elevation']
V_A_fnc = df2_fnc['aer_vol']
V_S_GPS_fnc = df2_fnc['subvol_gps']
V_E_GPS_fnc = df2_fnc['engvol_gps']
df2_fnc = df2_fnc.reset_index(drop=False)
time_fnc = df2_fnc.iloc[:,0]
V_T_fnc = V_A_fnc + V_S_GPS_fnc + V_E_GPS_fnc
#%% time series

# h(t)
# =============================================================================
# plt.plot(time,h, 'k')
# plt.xlabel("Date", size=12) 
# plt.ylabel("Water elevation (m a.s.l.)", size=12)
# ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
# plt.gcf().autofmt_xdate()
# =============================================================================
# plt.savefig("h(t).png", dpi=1200)

# V_S_float(t)
curve_fit = np.polyfit(time, V_S_float, 6)
f = np.poly1d(curve_fit)
V_S_float_fit = f(time)
r2 = r2_score(time, V_S_float_fit)
r2_rounded = round(r2, 3)

plt.plot(time, V_S_float, 'k')
plt.xlabel("Date", size=12) 
plt.ylabel("Subglacial floatation volume (x10$^7$m$^3$)", size=12)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
plt.gcf().autofmt_xdate()
#plt.savefig("V_S_float(t).png", dpi=300, bbox_inches = 'tight')

#V_A, V_S, V_E, V_I(t) for filling phase
# =============================================================================
# fig, ax1 = plt.subplots()
# ax1.plot(time, V_A, 'k', label = r'$V_{A}$')
# ax1.plot(time, V_S_GPS, 'purple', label = r'$V_{S}$')
# ax1.plot(time, V_E_GPS, 'green', label = r'$V_{E}$')
# ax1.plot(time, V_I, 'blue', label = r'$V_{I}$')
# ax1.set_xlabel("Date", size=12) 
# ax1.set_ylabel("Volume (x10$^7$m$^3$)", size=12)
# ax1.legend()
# #ax = plt.gca()
# ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
# plt.gcf().autofmt_xdate()
# 
# ax2 = ax1.twinx()
# ax2.plot(time, h, 'grey', label = "h")
# ax2.set_ylabel("Water elevation (m)", color = 'grey')
# ax2.tick_params(axis='y', labelcolor='grey')
# ax2.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
# plt.gcf().autofmt_xdate()
# =============================================================================
# plt.savefig("V_all(t).png", dpi=300)

#V_A, V_S, V_E, V_I(t) for draining phase
# =============================================================================
# plt.plot(time_draining, V_A_draining, 'k', label = r'$V_{A}$')
# plt.plot(time_draining, V_S_GPS_draining, 'purple', label = r'$V_{S}$')
# # plt.plot(time_draining, V_E_GPS_draining, 'green', label = r'$V_{E}$') # no more V_E
# plt.plot(time_draining, V_I_draining, 'blue', label = r'$V_{I}$')
# plt.xlabel("Date", size=12) 
# plt.ylabel("Volume (x10$^7$m$^3$)", size=12)
# plt.legend()
# ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# plt.gcf().autofmt_xdate()
# =============================================================================
# plt.savefig("V_all_filling(t).png", dpi=300)

#%% V_A(h)

salmon = matplotlib.colors.hex2color("#ef946c")
grey_b = matplotlib.colors.hex2color("#7087a4")

plt.plot(h, V_A, 'k')
plt.xlabel("Water level (m)")
plt.ylabel("Subaerial volume (m$^3$)")
plt.savefig("V_A(h).png", dpi=300)

curve_fit = np.polyfit(h, np.log(V_A), 1)
# y = ae^(bx) can be written as ln(y) = ln(a) + bx, so to get a and b:
a = np.exp(curve_fit[1])
b = curve_fit[0]
V_A_h = a * np.exp(b*h)
plt.plot(h, V_A_h, color = salmon, linewidth = 4)

#%% V_S(V_A)
# =============================================================================
# curve_fit = np.polyfit(V_A_filling_cont, V_S_GPS_filling_cont, 6)
# f = np.poly1d(curve_fit)
# V_S_filling_fit = f(V_A_filling_cont)
# r2 = r2_score(V_S_GPS_filling_cont, V_S_filling_fit)
# r2_rounded = round(r2, 3)
# 
# fig, ax = plt.subplots()
# ax.plot(V_A_filling_cont, V_S_GPS_filling_cont, 'k', label = "True")
# ax.plot(V_A_filling_cont, V_S_filling_fit, '--', label = "Modelled")
# # ax.text(0.02, 0.8, f'V_E = {c}e$^{d}V_A$', 
#  #        horizontalalignment='left',verticalalignment='center',
#  #     transform = ax.transAxes, size=10)
# ax.text(0.13,0.74, f"R$^2$ = {r2_rounded}", horizontalalignment='center',
#       verticalalignment='center',
#     transform = ax.transAxes, size = 10)
# ax.set_xlabel("Subaerial volume (m$^3$)")
# ax.set_ylabel("Subglacial volume (m$^3$)")
# ax.legend()
# =============================================================================
# plt.savefig("V_S(V_A)_filling_fit.png", dpi=300)

#%% V_S_float(h)
plt.plot(h, V_S_float, 'k')
plt.xlabel("Water elevation (m a.s.l.)", size=12)
plt.ylabel("Subglacial floatation volume (x10$^7$m$^3$)", size=12)

curve_fit = np.polyfit(h, np.log(V_S_float), 1)
# y = ae^(bx) can be written as ln(y) = ln(a) + bx, so to get a and b:
a = np.exp(curve_fit[1])
b = curve_fit[0]
V_S_float_h = a * np.exp(b*h)
plt.plot(h, V_S_float_h, color = salmon, linewidth = 0.1)
plt.text(0.02, 0.8, f'V_S_float = {a}e$^{b}h$', 
        horizontalalignment='left',verticalalignment='center',
    transform = ax.transAxes, size=10)

# plt.savefig("V_S_float(h).png", dpi=300)

#%%
# N = f(V_S_float)

# Fit the function a * np.log(sqrt(t^2 + c^2)) + b to x and y
t = np.log(V_S_float)
p0 = [8, 1470]
c = 262385.982
popt, pcov = curve_fit(lambda t, a, b: a * np.log(np.sqrt(t**2+c**2)) + b, 
                       V_S_float, h, p0 = p0)
a = popt[0]
b = popt[1]
#c = popt[2]
h_fitted = a * np.log(np.sqrt(V_S_float**2+c**2)) + b

ax = plt.axes()
ax.scatter(V_S_float, h, label='Raw data', s = 3)
ax.plot(V_S_float, h_fitted, 'k', label='Fitted curve')
ax.set_ylabel("Water elevation (m a.s.l.)", size=12)
ax.set_xlabel("Subglacial floatation volume (x10$^7$m$^3$)", size=12)
ax.legend()

#plt.text(0.02, 0.8, f'V_S_float = {a}e$^{b}h$', 
        #horizontalalignment='left',verticalalignment='center', size=10)

#plt.savefig("h(V_S_float)_v2.png", dpi=300)
#%% V_E(V_A)

# =============================================================================
# mod = LinearModel()
# params = mod.guess(V_E_GPS, x=V_A)
# result = mod.fit(V_E_GPS, params, x=V_A, )
# 
# a, b = np.polyfit(V_A, V_E_GPS, 1)
# fig, ax = plt.subplots(figsize = (7, 3.5))
# ax.plot(V_A, V_E_GPS, 'k')
# ax.plot(V_A, a*V_A+b, '--')
# ax.text(0.235, 0.8, 'V_E = ' + '{:.2f}'.format(b) + ' + {:.2f}'.format(a) + 'V_A', 
#         horizontalalignment='center',verticalalignment='center',
#      transform = ax.transAxes, size=10)
# ax.text(0.1,0.9, "R$^2$ = 0.982", horizontalalignment='center',
#      verticalalignment='center',
#      transform = ax.transAxes, size = 10)
# ax.set_xlabel("Subaerial volume (m$^3$)")
# ax.set_ylabel("Englacial volume (m$^3$)")
# =============================================================================
# plt.savefig("V_E(V_A).png", dpi=1200)

#%% V_T(h)

# =============================================================================
# curve_fit = np.polyfit(h_filling_cont, V_T_filling_cont, 4)
# f = np.poly1d(curve_fit)
# V_T_filling_fit = f(h_filling_cont)
# r2 = r2_score(V_T_filling_cont, V_T_filling_fit)
# r2_rounded = round(r2, 3)
# 
# fig, ax = plt.subplots()
# ax.plot(h_filling_cont,V_T_filling_cont, 'k', label = "True")
# ax.plot(h_filling_cont, V_T_filling_fit, '--', label = "Modelled")
# ax.text(0.13,0.74, f"R$^2$ = {r2_rounded}", horizontalalignment='center',
#        verticalalignment='center',
#      transform = ax.transAxes, size = 10)
# ax.set_xlabel("Water level (m)")
# ax.set_ylabel("Total volume (m$^3$)")
# ax.legend()
# 
# # plt.savefig("V_T(h)_filling.png", dpi=300)
# =============================================================================




