import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the hypothetical logistics dataset
df = pd.read_csv("week3_logistics_dataset.csv")

# Basic EDA
print(df.head())
print(df.info())
print(df.describe())

# Central tendency
print("\nMeans:")
print(df[["Shipment_Volume_kg", "Distance_km", "Delivery_Time_days",
          "Delay_days", "Total_Logistics_Cost_INR"]].mean())

print("\nMedians:")
print(df[["Shipment_Volume_kg", "Distance_km", "Delivery_Time_days",
          "Delay_days", "Total_Logistics_Cost_INR"]].median())

# Correlation
numeric = df.select_dtypes(include="number")
print("\nCorrelation matrix:")
print(numeric.corr())

# On-time delivery rate
on_time_rate = (df["On_Time"] == "Yes").mean() * 100
print(f"\nOverall on-time rate: {on_time_rate:.2f}%")

# 1. Delivery time distribution
plt.figure(figsize=(8,5))
plt.hist(df["Delivery_Time_days"], bins=20, edgecolor="black")
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (days)")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.show()

# 2. Cost by transport mode
plt.figure(figsize=(8,5))
df.boxplot(column="Total_Logistics_Cost_INR", by="Transport_Mode")
plt.suptitle("")
plt.title("Total Logistics Cost by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Total Logistics Cost (INR)")
plt.tight_layout()
plt.show()

# 3. Shipment volume vs cost
plt.figure(figsize=(8,5))
for mode in df["Transport_Mode"].unique():
    sub = df[df["Transport_Mode"] == mode]
    plt.scatter(sub["Shipment_Volume_kg"], sub["Total_Logistics_Cost_INR"],
                label=mode, alpha=0.65)
plt.title("Shipment Volume vs Total Logistics Cost")
plt.xlabel("Shipment Volume (kg)")
plt.ylabel("Total Logistics Cost (INR)")
plt.legend()
plt.tight_layout()
plt.show()

# 4. Average delay by region
region_delay = df.groupby("Region")["Delay_days"].mean().sort_values(ascending=False)
plt.figure(figsize=(8,5))
plt.bar(region_delay.index, region_delay.values)
plt.title("Average Delay by Region")
plt.xlabel("Region")
plt.ylabel("Average Delay (days)")
plt.tight_layout()
plt.show()

# 5. Distance vs delivery time
plt.figure(figsize=(8,5))
plt.scatter(df["Distance_km"], df["Delivery_Time_days"], alpha=0.65)
z = np.polyfit(df["Distance_km"], df["Delivery_Time_days"], 1)
xline = np.linspace(df["Distance_km"].min(), df["Distance_km"].max(), 100)
plt.plot(xline, np.poly1d(z)(xline))
plt.title("Distance vs Delivery Time")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery Time (days)")
plt.tight_layout()
plt.show()
