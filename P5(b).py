import matplotlib.pyplot as plt
import pandas as pd

car_data = pd.read_csv("/content/cars.csv")
cars = car_data["brand"].unique()[:4]  # Get the first 16 unique brands
brand_sales = car_data.groupby('brand')['selling_price'].sum()
brand_sales = brand_sales[cars]       # Filter sales data for the 16 brands
fig = plt.figure(figsize=(10, 7))
colors= ['#ff9999','#66b3ff','#ffcc99','#ffb3e6']
explode = (0, 0.1, 0.1, 0)
plt.pie(brand_sales, labels=cars, autopct="%1.1f%%" ,colors=colors, explode=explode)
plt.title("Car Sales Distribution by Brand (Top 16)")
plt.show()
car_data.head(6)