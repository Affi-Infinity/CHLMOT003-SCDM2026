# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:07:21 2026

@author: 4203750
"""
# import packages
import pandas as pd 

#Create a Pandas Dataframe:
 
filename = 'C:/Users/4203750/Documents/2026 Oceanography Honours/Week 4-8_Introduction_To_Data_Science/Exercises_And_Assignments/Data/Prac-1_CTD_data_v2_20260309.dat'
CTD_df = pd.read_csv(filename, delim_whitespace= True)
print(CTD_df)

print(CTD_df.head())

# Error warning use sep = '/s+' in the future. 