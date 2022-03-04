
import pandas as pd
mfp = "melb_data.csv"
md = pd.read_csv(mfp)

# drop any houses with missing data...
md = md.dropna(axis=0)

# pull out one column (prediction target)
y = md.Price

# grab features
mfeats = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = md[mfeats]

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, preds))

# this one (191669) is better than best decision tree (250000)??

# works reasonable well without tuning...
