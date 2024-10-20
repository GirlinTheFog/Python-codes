import matplotlib.pyplot as plt
import pandas as pd
car_data = pd.read_csv("/content/cars2.csv")
plt.hist(car_data['miles'][:17], color='pink',edgecolor='white',bins=5)
plt.title('Histogram for distance travelled in Kilometer')
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()
data.head(6)