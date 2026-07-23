#=====================================================
#                    economical_data
#=====================================================

from data_loader import *
#funct-14
def average_Electricity_Tariff(df):
    return df["Electricity_Tariff"].mean()

#funct-15
def total_expense(df, rate_per_unit=8):
    total_consumed = df["Electricity_Consumed_kWh"].sum()
    total_expense = total_consumed * rate_per_unit
    return total_expense

#funct-16
def efficiency(df):
    efficiency=df["Solar_Generation_kWh"]/df["Electricity_Consumed_kWh"]

#funct-17
def efficiency_percent(df):
    efficiency_percentage = df["Solar_Generation_kWh"] / df["Electricity_Consumed_kWh"] * 100

    return efficiency_percentage


#funct-18
def top5_efficient_days(df):
    df["efficiency"] = df["Solar_Generation_kWh"] / df["Peak_Power_kW"]
    efficient_days = df.sort_values("efficiency", ascending=False).head(5)
    return efficient_days[["Date", "efficiency"]]

def daily_savings(df):
    daily_savings = df["Electricity_Exported_kWh"] * df["Electricity_Tariff"]
    return daily_savings

# code for most and least efficient day
def efficient_and_not_efficient_days(df):
    df["efficiency"] = df["Solar_Generation_kWh"] / df["Peak_Power_kW"]
    efficient_day = df.sort_values("efficiency", ascending=False).head(1)
    print("most efficient day:")
    print(efficient_day[["Date", "efficiency"]])
    least_efficient_day = df.sort_values("efficiency", ascending=True).head(1)
    print("the least efficient days")
    print(least_efficient_day[["Date", "efficiency"]])
    return()
