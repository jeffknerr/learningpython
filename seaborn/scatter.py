"""
from kaggle data-vis mini tutorial

https://www.kaggle.com/learn/data-visualization
"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()

insurance_file = "insurance.csv"
insurance_data = pd.read_csv(insurance_file)

print(insurance_data.head())
print(insurance_data.tail())

#sb.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
#sb.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
#sb.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'],
#        hue=insurance_data['smoker'])
sb.lmplot(x='bmi', y='charges', hue='smoker', data=insurance_data)
plt.show()
sb.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
plt.show()
