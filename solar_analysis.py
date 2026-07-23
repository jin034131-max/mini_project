#===========================================================
 #                     solar_analysis
#===========================================================
import pandas as pd


#defining avg,min,max functions
#funt-1
def avg_solar_generation(df):
    return df["Solar_Generation_kWh"].mean()

#funct-2
def average_Peak_Power(df):
    return df["Peak_Power_kW"].mean()
#funct-3
def max_peak_power(df):
    return df["Peak_Power_kW"].max()

#funct-4
def total_Electricity_Exported(df):
    return df["Electricity_Exported_kWh"].sum()

#funct-5
def consumption_rate(df):
    for i in range(len(df)):            #loop_1///////////////////////
        date=df["Date"].iloc[i]
        data=df["Electricity_Consumed_kWh"].iloc[i]
        if data > 18:
            print(date, ":","highly consumed")
        else:
            print(date, ":", "used sustainably")
    return()
#funct-6
def net_consumption(df):
    return df["Electricity_Consumed_kWh"].sum()
#funct-7
def self_sufficiency(df):
    self_sufficiency = df["Solar_Generation_kWh"] / df["Electricity_Consumed_kWh"]
    return self_sufficiency

#funct-8
def avg_self_sufficiency(df):
    df["self_sufficiency"] = df["Solar_Generation_kWh"] / df["Electricity_Consumed_kWh"]
    avg_self_sufficiency = df["self_sufficiency"].mean()
    print("avg_self_sufficiency:", avg_self_sufficiency)
    if avg_self_sufficiency >=100:
        print("it is sufficient")
    elif avg_self_sufficiency >=50:
        print("it is partially sufficient")
    else:
        print("it is unsuffficient")
    return()
#funct-9
def highesst_production_month(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month_name()
    monthly_production = df.groupby("Month")["Solar_Generation_kWh"].sum()
    highesst_production_month = monthly_production.idxmax()
    return highesst_production_month

#solar performance index
def solar_performance_index(df):
    df["SPI"] = (0.5 * df["Solar_Generation_kWh"]) - (0.3 * df["Cloud_Cover"]) + (0.2 * df["Peak_Power_kW"])

    df["SPI_Category"] = ""

    i = 0
    while i < len(df):
        spi = df.loc[i, "SPI"]

        if spi >= 8:
            category = "Excellent"
        elif spi >= 5:
            category = "Good"
        elif spi >= 3:
            category = "Average"
        else:
            category = "Poor"
        df.loc[i, "SPI_Category"] = category
        i = i + 1

    print(df[["Date", "SPI", "SPI_Category"]])