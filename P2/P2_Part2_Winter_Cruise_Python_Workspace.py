# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:22:22 2026

@author: Elsie Chilwane
"""

# Import the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the dataset
filename = 'C:/Users/4203750/Documents/2026 Oceanography Honours/Week 4-8_Introduction_To_Data_Science/Exercises_And_Assignments/Data/SAA2_WC_2017_metocean_10min_avg.csv'
winter_cruise_df = pd.read_csv(filename, sep = r',', parse_dates=['TIME_SERVER'])

# Parse and set it as an index
winter_cruise_df = winter_cruise_df.set_index('TIME_SERVER')

# Inspect the dataframe:
print(winter_cruise_df.head())
print(winter_cruise_df.tail())

#Inspect the variables 
print(winter_cruise_df['TSG_TEMP'])
print(winter_cruise_df['TSG_SALINITY'])
print(winter_cruise_df['WIND_SPEED_TRUE'])
print(winter_cruise_df['AIR_TEMPERATURE'])

# Filtering the dates
july_df = winter_cruise_df.loc[:'2017-07-04']

# Plotting temperature timeseries
plt.style.use('grayscale')

fig, ax = plt.subplots()
ax.plot(july_df.index, july_df['TSG_TEMP'], color = 'orange')
ax.set_xlabel('Date (Days)')
ax.set_ylabel('Temperature(°C)')
ax.set_title('Winter Cruise July 4th SST')

fig.tight_layout()
fig.savefig("4th-July_Winter_Cruise_SST.png", dpi = 300) 
plt.show()

# Salinity Histogram 

# Set the bin range 
bins = np.arange(30, 35.5, 0.5)

fig, ax = plt.subplots(figsize=(10,5))
ax.hist(july_df['TSG_SALINITY'].dropna(), bins=bins, color= 'red')

ax.set_xlabel('Salinity (psu)')
ax.set_ylabel('Frequency')
ax.set_title('Salinity Histogram for SA Agulhas II Departure Dates')

# Add the limits according to the bin range
plt.xlim(30,35) 

plt.tight_layout()
plt.savefig('Salinity_histogram.png', dpi=300)
plt.show


# Scatter Plot

fig, ax = plt.subplots(figsize=(10,5))

july_scatter = ax.scatter(july_df['WIND_SPEED_TRUE'], july_df['AIR_TEMPERATURE'], c=july_df['LATITUDE'], cmap='viridis')

ax.set_xlabel('Wind Speed (m/s)')
ax.set_ylabel('Air Temperature(°C)')
ax.set_title('Scatterplot for SA Agulhas II Departure Dates')

# Adding latitude colorbar
cbar = fig.colorbar(july_scatter)
cbar.set_label('Latitude')

plt.tight_layout()
plt.savefig('scatter_wind_airtemp.png', dpi=300)

plt.show()


# Statistics Table 

# Reload my variables
temp = july_df['TSG_TEMP']
salinity = july_df['TSG_SALINITY']

# Calculate the temperature stats
temp_mean = temp.mean()
temp_std = temp.std

# Calculate the salinity stats
sali_mean = salinity.mean()
sali_std = salinity.std()

# Calculate the Interquartile Range
# IOR = Q3 - Q1
temp_iqr = temp.quantile(0.75) - temp.quantile(0.25)
sali_iqr = salinity.quantile(0.75) - salinity.quantile(0.25)
# Create a dataframe 
july_stats = pd.DataFrame({'Mean' : [temp_mean, sali_mean], 
                           'Standard Deviation' : [temp_std, sali_std],
                           'Interquartile Range' : [temp_iqr, sali_iqr]}, index = [
                               'Temperature', 'Salinity'])

print(july_stats)