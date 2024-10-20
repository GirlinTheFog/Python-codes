import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("/content/cars.csv")
df =pd.DataFrame(data)
X = list(df.iloc[:6, 0])
Y = list(df.iloc[:6, 4])
plt.bar(X,Y, color='green')
plt.title('Used Car Sales')
plt.xlabel('Car')
plt.ylabel('Number Sold')
plt.show()
data.head(6)