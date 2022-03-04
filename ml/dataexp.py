
# todo:
# without pandas, do all of this by hand


import pandas as pd
mfp = "melb_data.csv"
md = pd.read_csv(mfp)
print(md.describe())
print(md.columns)

# drop any houses with missing data...
md = md.dropna(axis=0)
#print(md.describe())

# pull out one column (prediction target)
y = md.Price
print(y)

# grab features
mfeats = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = md[mfeats]
print(X)
print(X.describe())
print(X.head())

# split data into training/validation
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


# # build the model
# from sklearn.tree import DecisionTreeRegressor
# mmodel = DecisionTreeRegressor(random_state=1)
# mmodel.fit(X, y)
# 
# # predict for first few rows???
# #print("predictions for first 5...")
# #print(mmodel.predict(X.head()))
# 
# from sklearn.metrics import mean_absolute_error
# predicted_home_prices = mmodel.predict(X)
# print(mean_absolute_error(y, predicted_home_prices))

# optimize tree size to find minimum mae
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

max_leaf_nodes = [5, 25, 50, 100, 250, 500, 1000, 2000, 5000]
bts = max_leaf_nodes[0]
bestmae = float("inf")
for mln in max_leaf_nodes:
    my_mae = get_mae(mln, train_X, val_X, train_y, val_y)
    print(mln, my_mae)
    if my_mae < bestmae:
        bts = mln
        bestmae = my_mae

print("best tree size:", bts)

