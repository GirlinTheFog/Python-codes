import matplotlib.pyplot as plt
import pandas as pd
car_data = pd.read_csv("/content/cars2.csv")
plt.scatter(car_data['age'][:17],car_data['sales'][:17], color='purple')
plt.title('Car Price vs Age')
plt.xlabel('Age(months)')
plt.ylabel('Sales(Price)')
plt.show()
data.head(6)