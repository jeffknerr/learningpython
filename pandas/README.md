
# Quick examples of using pandas


Note: most/all of this from 
https://www.kaggle.com/learn/pandas


## imports

```
import pandas as pd
```

## read csv

```
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
```

## examine data

```
>>> reviews.columns
Index(['country', 'description', 'designation', 'points', 'price', 'province',
       'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title',
       'variety', 'winery'],
      dtype='object')
>>> reviews.head()
    country                                        description  ...         variety               winery
0     Italy  Aromas include tropical fruit, broom, brimston...  ...     White Blend              Nicosia
1  Portugal  This is ripe and fruity, a wine that is smooth...  ...  Portuguese Red  Quinta dos Avidagos
2        US  Tart and snappy, the flavors of lime flesh and...  ...      Pinot Gris            Rainstorm
3        US  Pineapple rind, lemon pith and orange blossom ...  ...        Riesling           St. Julian
4        US  Much like the regular bottling from 2012, this...  ...      Pinot Noir         Sweet Cheeks

[5 rows x 13 columns]
>>> reviews.tail()
        country  ...                                    winery
129966  Germany  ...  Dr. H. Thanisch (Erben Müller-Burggraef)
129967       US  ...                                  Citation
129968   France  ...                           Domaine Gresser
129969   France  ...                      Domaine Marcel Deiss
129970   France  ...                          Domaine Schoffit

[5 rows x 13 columns]
>>> len(reviews)
129971
>>>
```

## grab one column

```
>>> reviews.country
0            Italy
1         Portugal
2               US
3               US
4               US
            ...
129966     Germany
129967          US
129968      France
129969      France
129970      France
Name: country, Length: 129971, dtype: object
>>> reviews.variety
0            White Blend
1         Portuguese Red
2             Pinot Gris
3               Riesling
4             Pinot Noir
               ...
129966          Riesling
129967        Pinot Noir
129968    Gewürztraminer
129969        Pinot Gris
129970    Gewürztraminer
Name: variety, Length: 129971, dtype: object
>>>
```

## summary functions

```
>>> len(reviews.variety.unique())
708
>>> reviews.price.min()
4.0
>>> reviews.price.max()
3300.0
>>> reviews.country.value_counts()
US                        54504
France                    22093
Italy                     19540
Spain                      6645
Portugal                   5691
...
```

## show specific columns

```
>>> cols = ['country', 'title', 'points', 'price']
>>> reviews.sort_values(by='points', ascending=False).loc[:, cols]
          country                                              title  points  price
114972   Portugal      Quinta do Noval 2011 Nacional Vintage  (Port)     100  650.0
89729      France  Salon 2006 Le Mesnil Blanc de Blancs Brut Char...     100  617.0
113929         US  Charles Smith 2006 Royal City Syrah (Columbia ...     100   80.0
45781       Italy  Biondi Santi 2010 Riserva  (Brunello di Montal...     100  550.0
123545         US  Cayuse 2008 Bionic Frog Syrah (Walla Walla Val...     100   80.0
...           ...                                                ...     ...    ...
128255  Argentina                    Viniterra 2007 Malbec (Mendoza)      80   13.0
128254  Argentina  François Lurton 2006 Gran Lurton Cabernet Sauv...      80   20.0
93686        Peru                   Tacama 2010 Brut Sparkling (Ica)      80   15.0
73865       Chile  De Martino 1999 Prima Reserva Merlot (Maipo Va...      80   13.0
128256         US   Bloomfield 2008 Chardonnay (Contra Costa County)      80   24.0

[129971 rows x 4 columns]
```

## answer questions...
 
```
>>> threshold = 94
>>> goodwines = reviews.loc[reviews.points >= threshold]
>>> len(goodwines)
6174
>>> goodwines.sort_values(by='points', ascending=False).loc[:, cols].groupby('country').country.count().sort_values()
country
Israel             1
Canada             3
Chile              8
Hungary            8
New Zealand        8
England           16
South Africa      19
Argentina         54
Australia         95
Spain            132
Germany          159
Portugal         240
Austria          283
Italy            840
France          1521
US              2787
```

The above looks terrible, but here's what I think it does:

- grab only rows with points greater than or equal to 94
- sort those wines by points (`sort_values(by='points'...)`)
- grab all rows, just the columns we want (`.loc[:, cols]`)
- group those by country and count how many of each country
- then finally sort the results of all of that...

