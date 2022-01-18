#! /usr/bin/python3

"""
programs and exercises from kaggle pandas tutorial:
https://www.kaggle.com/learn/pandas

J. Knerr
Winter, 2022

Show dataframe stats and use of pandas.
"""

import pandas as pd


def printline(char):
    """print a line of characters"""
    print(char*40)


def main():
    """main funtion..."""
    topn = 15
    reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
    print(reviews)
    printline("=")
    print("dataframe column names: ")
    print(reviews.columns)
    printline("=")

    print("Number of wines reviewed: %d" % len(reviews))
    print("Number of wine varieties: %d" % len(reviews.variety.unique()))
    print("Number of wines/country (top %d):" % topn)
    ccounts = reviews.groupby('country').country.count()
    print(ccounts.sort_values(ascending=False)[:topn])

    printline("=")
    # show min and max prices in dataframe
    print("min price: $%4d" % reviews.price.min())
    print("max price: $%4d" % reviews.price.max())

    # show wines with topn ratings
    what = ['country', 'title', 'points', 'price']
#   pd.set_option('display.max_rows', 1000)
#   pd.set_option('display.min_rows', 120)
    print(reviews.sort_values(by='points', ascending=False).loc[:, what])

    # how many ratings are >=90 for each country?
    printline("c")
    threshold = 94
    print('number of wines/country with rating >= %d' % threshold)
    count90s = reviews.loc[reviews.points >= threshold]
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.min_rows', 120)
    new = count90s.sort_values(by='points', ascending=False).loc[:, what]
    new = new.groupby('country').country.count()
    print(new.sort_values(ascending=False)[:])


main()
