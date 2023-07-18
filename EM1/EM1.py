# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:50:04 2022

@author: chlok

PHS2062: Lab 1 EM1
"""

# Import Statements
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import monashspa.PHS1011 as spa

# Part 1: Polarisation of Microwaves

# Malus' Law: I = I0*(np.cos(theta))**2

theta = [0, 15, 30, 45, 60, 75, 90]
u_theta = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
theta_rad = [x*(np.pi/180) for x in theta]
u_theta_rad = [x*(np.pi/180) for x in u_theta]
I0 = 180.9
u_I0 = 4.5

I = [207.025, 124.625, 82.4, 28.15, 20.1, 26.125, 2]
u_I = [4.5, 2.125, 1.5, 2.5, 1.875, 2.35, 2]


# Creating plots of raw data 
X = theta_rad
uX= u_theta_rad
Y = I
uY = u_I
title="Raw Data: Intensity vs Angle (degree)"
pltid=1
fname='rawdata1.png'

plt.figure(pltid)
plt.title(title)
plt.errorbar(theta,Y, xerr=uX,yerr=uY, marker="o", linestyle="None", color="red",label="data")
plt.xlabel("Angle (degree)")
plt.ylabel("Intensity")

# Perform a linear fit 

stat_fit_results = spa.linear_fit(X, Y, u_y = uY)
stat_y_fit = stat_fit_results.best_fit
stat_u_y_fit = stat_fit_results.eval_uncertainty(sigma=1)
stat_parameters_from_fit = spa.get_fit_parameters(stat_fit_results)
stat_slope = stat_parameters_from_fit["slope"]
stat_u_slope = stat_parameters_from_fit["u_slope"]
stat_intercept = stat_parameters_from_fit["intercept"]
stat_u_intercept = stat_parameters_from_fit["u_intercept"]

# Plotting Malus' Law: I = I0*(np.cos(theta))**2 * fit into linear best fit
malus_I = I0*(np.cos(theta_rad))**2
#u_malus_I = np.sqrt( ((np.cos(theta_rad))**2 * u_I0)**2 + (-2*I0*np.sin(theta_rad)*np.cos(theta_rad) * u_theta_rad)**2)
u_malus_I = [4.50000000e+00, 4.27210913e+00, 3.64139089e+00, 2.74856995e+00, 1.77051620e+00, 8.44927207e-01, 1.93328905e-16]

malus_fit_results = spa.linear_fit(X, malus_I, u_y = u_malus_I)
malus_y_fit = malus_fit_results.best_fit
malus_u_y_fit = malus_fit_results.eval_uncertainty(sigma=1)
malus_parameters_from_fit = spa.get_fit_parameters(malus_fit_results)
malus_slope = malus_parameters_from_fit["slope"]
malus_u_slope = malus_parameters_from_fit["u_slope"]
malus_intercept = malus_parameters_from_fit["intercept"]
malus_u_intercept = malus_parameters_from_fit["u_intercept"]

# Plot of Linear Transform x and y with super imposed Linear fit 

plt.figure(2)
plt.title("Figure 2: Plots of Linear Fit for Raw Data and Malus Formula")
plt.errorbar(X, Y, yerr=uY, marker=".", linestyle="None", color="red", label="Transformed Data")
plt.plot(X, stat_y_fit, marker="None", linestyle="-", color="red",label="linear fit for data")
plt.fill_between(X,stat_y_fit-stat_u_y_fit,stat_y_fit+stat_u_y_fit, color="pink",label="uncertainty in linear fit")
plt.errorbar(X, malus_I, yerr=u_malus_I, marker=".", linestyle="None", color="blue", label="Malus Formula")
plt.plot(X, malus_y_fit, marker="None", linestyle="-", color="blue",label="linear fit for Malus Formula")
plt.fill_between(X,malus_y_fit-malus_u_y_fit,malus_y_fit+malus_u_y_fit, color="cyan",label="uncertainty in linear fit in Malus Formula")
plt.xlabel("Angle (rad)")
plt.ylabel("Intensity")
leg = plt.legend(bbox_to_anchor=(1,1))
plt.show()

# Print equation of linearised fits
print("\nFit Results:\n")
print("Raw Data Fit:\ny =",round(stat_slope,2),"x","+/-",round(stat_u_slope,2),"+",round(stat_intercept,2),"+/-", round(stat_u_intercept,2))
print("Malus Law Fit:\ny =",round(malus_slope,2),"x","+/-",'%s' % float('%.3g' % malus_u_slope),"+",round(malus_intercept,2),"+/-", '%s' % float('%.3g' % malus_u_intercept))
