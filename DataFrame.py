import pandas as pd


df = pd.read_csv("C:\\Users\\HP\\Desktop\\Big Data\\uber.csv")


print(df.head())


print("Dataset shape:", df.shape)

print("=== Dataset Structure ===")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print()

print("=== Data Types and Memory Info ===")
print(df.info())
print()

print("=== Missing Values Per Column ===")
print(df.isnull().sum())
print()

print("=== Check for Duplicate Rows ===")
print("Duplicates:", df.duplicated().sum())

# 1. Drop missing values
df_cleaned = df.dropna()
print("After dropping missing:", df_cleaned.shape)

# 2. Drop duplicates
df_cleaned = df_cleaned.drop_duplicates()
print("After dropping duplicates:", df_cleaned.shape)

# 3. Remove invalid fare/passenger counts
df_cleaned = df_cleaned[(df_cleaned['fare_amount'] > 0) & 
                        (df_cleaned['passenger_count'] > 0)]
print("After removing invalid fare/passenger_count:", df_cleaned.shape)

# 4. Export to CSV
df_cleaned.to_csv("uber_cleaned.csv", index=False)
print("Cleaned dataset saved as 'uber_cleaned.csv'")

# 2a. 

import numpy as np

# Descriptive statistics
print("=== Descriptive Statistics ===")
print(df_cleaned.describe())

# Median and Mode (fare and passenger count)
print("\nMedian fare:", df_cleaned['fare_amount'].median())
print("Mode fare:", df_cleaned['fare_amount'].mode()[0])

print("\nMedian passengers:", df_cleaned['passenger_count'].median())
print("Mode passengers:", df_cleaned['passenger_count'].mode()[0])

# Quartiles
print("\n=== Quartiles ===")
print(df_cleaned['fare_amount'].quantile([0.25, 0.5, 0.75]))

# Outlier check: fares above 100 dollars
high_fares = df_cleaned[df_cleaned['fare_amount'] > 100]
print("\nHigh fare rides (> $100):", high_fares.shape[0])

# 2b Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("uber_cleaned.csv")

# Set style
sns.set(style="whitegrid")

# === 1. Fare Amount Distribution (Histogram) ===
plt.figure(figsize=(10, 6))
sns.histplot(df['fare_amount'], bins=50, kde=True)
plt.title("Fare Amount Distribution")
plt.xlabel("Fare ($)")
plt.ylabel("Frequency")
plt.xlim(0, 100)  # Limit extreme fares
plt.show()

# === 2. Boxplot of Fare Amount (outlier detection) ===
plt.figure(figsize=(10, 4))
sns.boxplot(x=df['fare_amount'])
plt.title("Fare Amount Boxplot")
plt.xlim(0, 100)
plt.show()


# 2c Analyze Relationships Between Key Variables

import numpy as np

# Estimate trip distance using straight-line (Euclidean) distance
df['distance'] = np.sqrt(
    (df['dropoff_longitude'] - df['pickup_longitude'])**2 +
    (df['dropoff_latitude'] - df['pickup_latitude'])**2
)

print("Distance column added.")

# 1. Fare vs. Distance
plt.figure(figsize=(10, 6))
sns.scatterplot(x='distance', y='fare_amount', data=df, alpha=0.5)
plt.title("Fare Amount vs. Distance")
plt.xlabel("Distance (approx.)")
plt.ylabel("Fare ($)")
plt.xlim(0, 0.3)
plt.ylim(0, 100)
plt.show()

# Fare vs. Time of Day

# Convert pickup_datetime to datetime format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Extract hour
df['hour'] = df['pickup_datetime'].dt.hour


# Fare vs. Passenger Count

plt.figure(figsize=(10, 6))
sns.boxplot(x='passenger_count', y='fare_amount', data=df)
plt.title("Fare Amount by Passenger Count")
plt.xlabel("Passengers")
plt.ylabel("Fare ($)")
plt.ylim(0, 100)
plt.show()

# 3 Feature Engineering

# Ensure pickup_datetime is in datetime format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Extract features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek  # 0=Monday, 6=Sunday

# Peak vs. Off-Peak Time


# Define peak time as 7-9 AM and 4-7 PM
def is_peak(hour):
    return (7 <= hour <= 9) or (16 <= hour <= 19)

df['is_peak'] = df['hour'].apply(lambda x: 'Peak' if is_peak(x) else 'Off-Peak')

# save Dataset for Power BI

df.to_csv("uber_enhanced.csv", index=False)
print("Enhanced dataset saved as 'uber_enhanced.csv'")



