
# Quick examples of using seaborn to make plots.


Note: most/all of this from 
[https://www.kaggle.com/learn/data-visualization]
(https://www.kaggle.com/learn/data-visualization)


Imports:

```
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
pd.plotting.register_matplotlib_converters()
```

Read flight data into pandas dataframe from csv file:

```
datafile = "clean_flights.csv"
delays = pd.read_csv(datafile, index_col="MONTH")
```

or the museum data (just grab a subset of the columns):

```
mf = "museum-visitors.csv"
md = pd.read_csv(mf, index_col="Month", parse_dates=True)
museum_data = md[['Avila Adobe', 'Firehouse Museum',
                  'Chinese American Museum',
                  'America Tropical Interpretive Center']]
```

## lineplot

```
sb.lineplot(data=museum_data)
plt.title("Museum Attendance Stats")
plt.ylabel("Num. Visitors")
plt.xlabel("Date")
plt.show()
```

## bar

```
airline = "NK"
sb.barplot(x=delays.index, y=delays[airline])
plt.title("avg delay vs month for %s" % airline)
plt.xlabel("month")
plt.ylabel("average delay (minutes)")
plt.show()
```

## heatmap

```
plt.title("avg delay for all months vs airlines")
plt.xlabel("airline")
plt.ylabel("month")
sb.heatmap(data=delays, annot=True)
plt.show()
```
