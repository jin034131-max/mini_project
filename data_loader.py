import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
df=pd.read_csv('solar_energy_data_fixed(1).csv')
print("=================================================================")
print("                   |  original data   |                            ")
print("=================================================================")
print(df)

df["efficiency"]=df["Solar_Generation_kWh"]/df["Peak_Power_kW"]
print(df)           #data having efficiency