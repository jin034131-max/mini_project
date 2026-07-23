#=============================================================
#                         graphs
#=============================================================
import matplotlib.pyplot as plt
import pandas as pd

# 1. Line Graph - Daily solar generation
def daily_generation(df):
    plt.plot(df['Date'], df['Solar_Generation_kWh'], color='orange')
    plt.title('Daily Solar Generation')
    plt.xlabel('Date')
    plt.ylabel('Solar Generation (kWh)')
    plt.tight_layout()
    plt.savefig('figures/generation_trend.png')

# 2. Scatter Plot - Cloud cover vs solar generation
def cloud_vs_generation(df):
    plt.scatter(df['Cloud_Cover'], df['Solar_Generation_kWh'], alpha=0.6, color='blue')
    plt.title('Cloud Cover vs Solar Generation')
    plt.xlabel('Cloud Cover (%)')
    plt.ylabel('Solar Generation (kWh)')
    plt.savefig('figures/weather_vs_generation.png')

# 3. Bar graph - Monthly consumption
def monthly_consumption(df):
    monthly = df.groupby('Month')['Electricity_Consumed_kWh'].sum()
    plt.bar(monthly.index, monthly.values, color='green')
    plt.title('Monthly Electricity Consumption')
    plt.xlabel('Month')
    plt.ylabel('Electricity Consumed (kWh)')
    plt.savefig('figures/monthly_consumption.png')

# 4. Histogram - daily savings
def daily_savings_graph(df):
    df['Daily_Savings'] = df['Electricity_Exported_kWh'] * df['Electricity_Tariff']
    plt.hist(df['Daily_Savings'], bins=15, color='purple', edgecolor='black')
    plt.title('Distribution of Daily Savings')
    plt.xlabel('Daily Savings (Rs)')
    plt.ylabel('Number of Days')
    plt.savefig('figures/savings_analysis.png')

# 5 Box Plot - Solar efficiency
def efficiency_graph(df):
    df['Solar_Efficiency'] = df['Solar_Generation_kWh'] / df['Peak_Power_kW']
    plt.boxplot(df['Solar_Efficiency'])
    plt.title('Solar Efficiency Distribution')
    plt.ylabel('Efficiency')
    plt.savefig('figures/efficiency_distribution.png')