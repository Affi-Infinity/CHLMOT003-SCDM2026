# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:00:45 2026

@author: Elsie Chilwane
"""

#Import all the packages:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Create a dataframe 
filename = 'C:/Users/4203750/Documents/2026 Oceanography Honours/Week 4-8_Introduction_To_Data_Science/Exercises_And_Assignments/Data/Prac-1_CTD_data_v2_20260309.dat'
CTD_df = pd.read_csv(filename, delim_whitespace= True)

# Have a look at the dataframe
print(CTD_df.columns)
print(CTD_df.head)

#Have a look at the columns
print(CTD_df['Time'])
print(CTD_df['Date'])
print(CTD_df['Depth(m)'])
print(CTD_df['Temperature(°C)'])
print(CTD_df['Salinity(psu)'])

# Define the variables from dataframe
depth = CTD_df['Depth(m)']
temperature = CTD_df['Temperature(°C)']
salinity = CTD_df['Salinity(psu)']

#Beginning of Plot Analysis

fig, ax = plt.subplots(1,2, sharey=True, figsize=(8,6))

# Creating my temperature profile
ax[0].plot(temperature, depth, color='blue')
ax[0].set_xlabel('Temperature(°C)')
ax[0].set_ylabel('Depth(m)')
ax[0].set_title( 'Temperature Profile')

#Creating my Salinity profile
ax[1].plot(salinity, depth, color= 'green')
ax[1].set_xlabel('Salinity(psu)')
ax[1].set_ylabel('Depth(m)')
ax[1].set_title('Salinity Profile')

plt.tight_layout() # Suggestion from ChatGPT, adjusts the parameters of figure to fit into place
plt.savefig('Temperature_and_Salinity.png', dpi = 300)
plt.show()