
# import libraries
import numpy as np
import pandas as pd



def outlier_percentile_90100(df_var):
    var = df_var.values
    var = np.sort(var,axis = None)
    for i in range(90,100):
        print("{} percentile value is {}".format(i,var[int(len(var)*(float(i)/100))]))
    print("100 percentile value is ",var[-1])




def outlier_percentile_99(df_var):
    var = df_var.values
    var = np.sort(var,axis = None)
    for i in np.arange(0.0, 1.0, 0.1):
        print("{} percentile value is {}".format(99+i,var[int(len(var)*(float(99+i)/100))]))
    print("100 percentile value is ",var[-1])