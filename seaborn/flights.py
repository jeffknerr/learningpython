"""
from kaggle data-vis mini tutorial

https://www.kaggle.com/learn/data-visualization
data: originally 5M flights from DOT file
      cleaned and averaged for each airline, for each month of 2015
"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()

datafile = "clean_flights.csv"
delays = pd.read_csv(datafile, index_col="MONTH")
print(delays.head())
print(delays.columns)

# bar
airline = "NK"
sb.barplot(x=delays.index, y=delays[airline])
plt.title("avg delay vs month for %s" % airline)
plt.xlabel("month")
plt.ylabel("average delay (minutes)")
plt.show()

# heatmap
plt.title("avg delay for all months vs airlines")
plt.xlabel("airline")
plt.ylabel("month")
sb.heatmap(data=delays, annot=True)
plt.show()
