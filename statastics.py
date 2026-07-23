#=========================================================================
#                           statistical_analysis
#=========================================================================

#funct-19
def statastical_analysis(df):
    # 1. Mean
    mean_generation = df["Solar_Generation_kWh"].mean()
    print("Mean Daily Generation :", round(mean_generation, 2), "kWh")

    # 2. Median
    median_consumption = df["Electricity_Consumed_kWh"].median()
    print("Median Consumption :", round(median_consumption, 2), "kWh")

    # 3. Mode
    mode_generation = df["Solar_Generation_kWh"].mode()[0]
    print("Mode Generation :", mode_generation, "kWh")

    # 4. Variance
    variance = df["Solar_Generation_kWh"].var()
    print("Variance :", round(variance, 2))

    # 5. Standard Deviation
    std = df["Peak_Power_kW"].std()
    print("Standard Deviation of Peak Power :", round(std, 2), "kW")

    # 6. Minimum
    minimum = df["Solar_Generation_kWh"].min()
    print("Minimum Generation :", minimum, "kWh")

    # 7. Maximum
    maximum = df["Solar_Generation_kWh"].max()
    print("Maximum Generation :", maximum, "kWh")

