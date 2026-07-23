#===========================================================
#                     weather_analysis
#===========================================================

#funct-10
def Maximum_Temperature(df):
    return df["Maximum_Temperature_C"].max()

#funct-11
def Minimum_Temperature(df):
    return df["Minimum_Temperature_C"].min()

#funct-12
def Average_Temperature(df):
    return df["Average_Temperature_C"].mean()

#funct-13
def productivity(df):
    for i in range(len(df)):        #loop-2////////for productivity
        date = df["Date"][i]
        cloud = df["Cloud_Cover"][i]

        if cloud < 50:
            print(date, "-", "Good days for production")
        else:
            print(date, "-", "Low days for production")
    return()

#funct_14
def rainfall_intensity(df):
    return df["Rainfall_Intensity"].mean()

#funct-15
def humidity(df):
    for humidity in df["Humidity"]:     #loop-3////////for weather & solar relaton
        if humidity < 50:
            print("low humidity", humidity)
        else:
            print("high humidity", humidity)

    return humidity

#funct_16
def weather_impact_analysis(df):
    # Correlation
    corr_temp = df["Maximum_Temperature_C"].corr(df["Solar_Generation_kWh"])
    corr_cloud = df["Cloud_Cover"].corr(df["Solar_Generation_kWh"])
    corr_rain = df["Rainfall_mm"].corr(df["Solar_Generation_kWh"])
    corr_humidity = df["Humidity"].corr(df["Solar_Generation_kWh"])

    return corr_temp, corr_cloud, corr_rain, corr_humidity

#funct-17
def temperature_difference(df):
    temperature_difference = df["Maximum_Temperature_C"] - df["Minimum_Temperature_C"]
    return temperature_difference
#funct-18
def check_relation_strength(corr_value, factor_name):
    corr_abs = abs(corr_value)
    if corr_abs >= 0.5 and corr_abs <= 1.0:
        print(f"{factor_name}: Strong relation with value = {round(corr_value, 2)}")
    elif corr_abs > 0 and corr_abs < 0.5:
        print(f"{factor_name}: Weak relation with value = {round(corr_value, 2)}")
    else:
        print(f"{factor_name}: No relation with value = {round(corr_value, 2)}")
    return()
#funct-19
def temp_correlation(df):
    corr_temp = df["Solar_Generation_kWh"].corr(df["Maximum_Temperature_C"])
    if corr_temp > 0.3:
        print("it has a good affect on solar generation")
    elif corr_temp < 0.3 and corr_temp > 1:
        print("it has some on solar generation")
    elif corr_temp ==0:
        print("it has no effect on solar generation")
    elif corr_temp<0:
        print("it has -ve effect on solar generation")
    else:
        print("error")
    return corr_temp
#funct-20
def cloud_rainfall_correlation(df):
    corr_cloud = df["Solar_Generation_kWh"].corr(df["Cloud_Cover"])
    corr_rain = df["Solar_Generation_kWh"].corr(df["Rainfall_mm"])

    print("\nConclusion:")
    if corr_cloud < 0:
        print("it has -ve effect on solar generation ")
    elif corr_cloud >0:
        print("it has +ve effect on solar generation ")
    elif corr_cloud ==0:
        print("it has no effect on solar generation")

    if corr_rain < 0:
        print("it has -ve effect on solar generation")
    elif corr_rain >0:
        print("it has +ve effect on solar generation")
    elif corr_rain ==0:
        print("it has no effect on solar generation")
    else:
        print("error")
    (print("the corelation with cloud cover is :",corr_cloud), print("the corelation with rainfall is:",corr_rain))
    return("done")








