import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

dataset_path = "sports_car_prices.csv"  
df = pd.read_csv(dataset_path)
print(df.head())


df.drop_duplicates(inplace=True)
df.dropna(inplace=True)


if 'price' in df.columns:
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
if 'horsepower' in df.columns:
    df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df.dropna(inplace=True)  


summary_stats = df.describe(include='all')
print(summary_stats)


avg_price_per_make = df.groupby('make')['price'].mean()
print(avg_price_per_make)


avg_hp_per_year = df.groupby('year')['horsepower'].mean()
print(avg_hp_per_year)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['horsepower'], y=df['price'])


X = df[['horsepower']]
y = df['price']
model = LinearRegression()
model.fit(X, y)
plt.plot(df['horsepower'], model.predict(X), color='red')

plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.title('Price vs Horsepower')
plt.show()


plt.figure(figsize=(10, 6))
df['0-60 mph'].plot(kind='hist', bins=np.arange(df['0-60 mph'].min(), df['0-60 mph'].max(), 0.5))
plt.xlabel('0-60 MPH Time (seconds)')
plt.title('Distribution of 0-60 MPH Times')
plt.show()


df_filtered = df[df['price'] > 500000].sort_values(by='horsepower', ascending=False)
print(df_filtered)


df.to_csv("cleaned_sports_car_prices.csv", index=False)
