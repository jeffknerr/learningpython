"""
from kaggle data-vis mini tutorial

https://www.kaggle.com/learn/data-visualization
"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()

mf = "museum-visitors.csv"
md = pd.read_csv(mf, index_col="Month", parse_dates=True)
museum_data = md[['Avila Adobe', 'Firehouse Museum',
                  'Chinese American Museum',
                  'America Tropical Interpretive Center']]
print(museum_data.head())
print(museum_data.tail())
sb.lineplot(data=museum_data)
print(list(museum_data.columns))

plt.title("Museum Attendance Stats")
plt.ylabel("Num. Visitors")
plt.xlabel("Date")
plt.show()

# subset of data
plt.title("Museum Attendance Stats [subset]")
plt.ylabel("Num. Visitors")
plt.xlabel("Date")
sb.lineplot(data=museum_data['Avila Adobe'], label='Avila')
sb.lineplot(data=museum_data['Firehouse Museum'], label='Firehouse')
plt.show()
