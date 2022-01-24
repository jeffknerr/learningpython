"""
from kaggle data-vis mini tutorial

https://www.kaggle.com/learn/data-visualization
"""

import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()

# https://www.kaggle.com/kanncaa1/statistical-learning-tutorial-for-beginners/data
# Breast Cancer Wisconsin (Diagnostic) Data Set
df = "data.csv"
cd = pd.read_csv(df, index_col="id")

print(cd.head())
print(cd.tail())

# split into two datasets
ben = cd.loc[cd.diagnosis == 'B']
mal = cd.loc[cd.diagnosis == 'M']
print(ben.head())
print(mal.head())

# now make a plot or two
sb.distplot(a=ben['area_mean'], label='benign', kde=False)
sb.distplot(a=mal['area_mean'], label='malignant', kde=False)
plt.legend()
plt.show()

sb.kdeplot(data=ben['radius_worst'], shade=True, label='benign')
sb.kdeplot(data=mal['radius_worst'], shade=True, label='malignant')
plt.legend()
plt.show()
