# import libraries
import numpy as np
import pandas as pd

# def hello():
#     print('salam')

def mean_fnc(df_column):
    mean_df = df_column.mean()
    return mean_df
    
def std_fnc(df_column):
    std_df = df_column.std()   
    return std_df

def sdt1_fnc(df_column,mean_df,std_df) :   
    lower_limit = mean_df - 1 * std_df
    upper_limit = mean_df + 1 * std_df
    sdt1_result=((df_column >= lower_limit) & (df_column <= upper_limit)).mean()
    return sdt1_result
    
    
def sdt2_fnc(df_column,mean_df,std_df):
    lower_limit = mean_df - 2 * std_df
    upper_limit = mean_df + 2 * std_df
    sdt2_result=((df_column >= lower_limit) & (df_column <= upper_limit)).mean()
    return sdt2_result
    
    
def sdt3_fnc(df_column,mean_df,std_df):
    lower_limit = mean_df - 3 * std_df
    upper_limit = mean_df + 3 * std_df
    sdt3_result=((df_column >= lower_limit) & (df_column <= upper_limit)).mean()
    return sdt3_result