

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s

# Load data
df = pd.read_csv('vehicles_us.csv')

# Clean column names
df.columns = df.columns.str.strip()

# Ensure numeric data
df['cylinders'] = pd.to_numeric(df['cylinders'], errors='coerce')
df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce' )
df['is_4wd'] = pd.to_numeric(df['is_4wd'], errors='coerce')

# Remove duplicates
df.drop_duplicates(inplace=True)

#Mean_Median
print(df['model_year'].mean())
print(df['cylinders'].median())
print(df['odometer'].mean())

#Fill the missing value on car color col

df['paint_color'] = df['paint_color'].astype(str)
df['paint_color'] = df['paint_color'].fillna('unknown')



# Fill missing values
df['cylinders'] = df['cylinders'].fillna(6)
df['model_year'] = df['model_year'].fillna(2009)
df['odometer'] = df['odometer'].fillna(115553)
df['is_4wd'] = df['is_4wd'].fillna(0)

# Remove outliers in 'model_year'
Q1 = df['model_year'].quantile(0.25)
Q3 = df['model_year'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['model_year'] >= (Q1 - 1.5 * IQR)) & (df['model_year'] <= (Q3 + 1.5 * IQR))]

# Remove outliers in 'price'
Q1_price = df['price'].quantile(0.25)
Q3_price = df['price'].quantile(0.75)
IQR_price = Q3_price - Q1_price
df = df[(df['price'] >= (Q1_price - 1.5 * IQR_price)) & (df['price'] <= (Q3_price + 1.5 * IQR_price))]

# Confirm changes
print(df.isna().sum())

# Histogram: Distribution of Model Year
plt.hist(df['model_year'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Model Year')
plt.xlabel('Model Year')
plt.ylabel('Frequency')
plt.show()

# Scatterplot: Price vs. Odometer
plt.scatter(df['price'], df['odometer'], alpha=0.5)
plt.title('Price vs. Odometer')
plt.xlabel('Price')
plt.ylabel('Odometer (miles)')
plt.show()


