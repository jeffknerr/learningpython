
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

## or create from dictionary

```
>>> data = {'yes':[10,20,33], 'no':[4,13,9], 'maybe':[12,0,9]}
>>> surveys = pd.DataFrame(data)
>>> surveys
   yes  no  maybe
0   10   4     12
1   20  13      0
2   33   9      9
```

DatFrame = table, Series = list.

```
>>> letters = list("abcdefg")
>>> s = pd.Series(letters)
>>> s
0    a
1    b
2    c
3    d
4    e
5    f
6    g
dtype: object
>>>
>>> s = pd.Series(letters, index=list("ABCDEFG"), name='Letters')
>>> s
A    a
B    b
C    c
D    d
E    e
F    f
G    g
Name: Letters, dtype: object
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

## grab one row

```
>>> surveys
   yes  no  maybe
0   10   4     12
1   20  13      0
2   33   9      9
>>> surveys.iloc[0]
yes      10
no        4
maybe    12
Name: 0, dtype: int64
>>> surveys.iloc[2]
yes      33
no        9
maybe     9
Name: 2, dtype: int64
```
Or use `iloc` to grab a column

```
>>> surveys.iloc[:, 2]
0    12
1     0
2     9
Name: maybe, dtype: int64
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
>>> surveys.loc[:, "yes"]
0    10
1    20
2    33
Name: yes, dtype: int64
>>> surveys.loc[:, "no"]
0     4
1    13
2     9
Name: no, dtype: int64
>>> surveys.loc[:, "maybe"]
0    12
1     0
2     9
Name: maybe, dtype: int64
>>> surveys.loc[:, ["yes","maybe"]]
   yes  maybe
0   10     12
1   20      0
2   33      9
```

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

## conditional selections

```
>>> reviews.loc[reviews.country == "Canada"]
       country                                        description  ...                  variety           winery
454     Canada  An aromatic knockout with notes of peach, papa...  ...                    Vidal       Pillitteri
2616    Canada  A slightly earthy, spicy nose leads, followed ...  ...  Gewürztraminer-Riesling       Pillitteri
5129    Canada  The Okanagan has the capability to produce del...  ...               Pinot Noir    Burrowing Owl
...        ...                                                ...  ...                      ...              ...
129485  Canada  A youthful and appealing wine with notes of or...  ...                 Riesling  Henry of Pelham
129528  Canada  A delicious though somewhat reserved wine with...  ...                    Vidal  Henry of Pelham
129581  Canada  Smooth and engaging, this offers classic varie...  ...                    Syrah    Burrowing Owl

[257 rows x 13 columns]
>>>
>>> reviews.loc[(reviews.country == "Canada") & (reviews.points >= 94)]
      country                                        description  ...                   variety          winery
7878   Canada  Smooth as silk and deeply concentrated, this o...  ...                  Riesling     Cave Spring
27558  Canada  Portfolio is a full-on, five-grape, Bordeaux-s...  ...  Bordeaux-style Red Blend  Laughing Stock
38210  Canada  This 100% varietal cuvée is smoky, supple and ...  ...                     Syrah    Le Vieux Pin

[3 rows x 13 columns]
```

## `isin()` and `notnull()`

```
>>> reviews.loc[reviews.country.isin(['Israel','Chile'])]
       country                                        description  ...              variety          winery
36       Chile  White flower, lychee and apple aromas carry th...  ...  Viognier-Chardonnay         Estampa
44       Chile  A berry aroma comes with cola and herb notes. ...  ...               Merlot        Sundance
51       Chile  This is much different than Casa Silva's 2009 ...  ...         Petit Verdot      Casa Silva
58       Chile  Lightly herbal strawberry and raspberry aromas...  ...           Pinot Noir   Tres Palacios
80       Chile  Caramelized oak and vanilla aromas are front a...  ...            Carmenère          Aresti
...        ...                                                ...  ...                  ...             ...
129640   Chile  The 2012 vintage was so hot in Chile that harv...  ...      Sauvignon Blanc   Concha y Toro
129812   Chile  Opens with a light, herbal bouquet that featur...  ...            Red Blend    Santa Alicia
129830   Chile  After several years spent in Chile's land of t...  ...      Sauvignon Blanc  Santa Carolina
129944  Israel  Deep garnet in the glass, this has a nose of b...  ...               Shiraz          Barkan
129963  Israel  A bouquet of black cherry, tart cranberry and ...  ...   Cabernet Sauvignon          Dalton

[4977 rows x 13 columns]
>>> reviews.loc[reviews.price.notnull()]
         country  ...                                    winery
1       Portugal  ...                       Quinta dos Avidagos
2             US  ...                                 Rainstorm
3             US  ...                                St. Julian
4             US  ...                              Sweet Cheeks
5          Spain  ...                                    Tandem
...          ...  ...                                       ...
129966   Germany  ...  Dr. H. Thanisch (Erben Müller-Burggraef)
129967        US  ...                                  Citation
129968    France  ...                           Domaine Gresser
129969    France  ...                      Domaine Marcel Deiss
129970    France  ...                          Domaine Schoffit

[120975 rows x 13 columns]
```

## map 

Change all values in a column, create new (transformed) Series/DataFrame:

```
>>> reviews.points
0         87
1         87
2         87
3         87
4         87
          ..
129966    90
129967    90
129968    90
129969    90
129970    90
Name: points, Length: 129971, dtype: int64
>>> reviews.points.map(lambda p: p-5)
0         82
1         82
2         82
3         82
4         82
          ..
129966    85
129967    85
129968    85
129969    85
129970    85
Name: points, Length: 129971, dtype: int64
>>> reviews.points
0         87
1         87
2         87
3         87
4         87
          ..
129966    90
129967    90
129968    90
129969    90
129970    90
Name: points, Length: 129971, dtype: int64

```

Use `apply()` to transorm whole DataFrame by calling custom method on each row.

```
>>> def lc(row):
...    row.country = str(row.country).lower()
...    return row
...
>>> reviews.apply(lc, axis='columns')
         country  ...                                    winery
0          italy  ...                                   Nicosia
1       portugal  ...                       Quinta dos Avidagos
2             us  ...                                 Rainstorm
3             us  ...                                St. Julian
4             us  ...                              Sweet Cheeks
...          ...  ...                                       ...
129966   germany  ...  Dr. H. Thanisch (Erben Müller-Burggraef)
129967        us  ...                                  Citation
129968    france  ...                           Domaine Gresser
129969    france  ...                      Domaine Marcel Deiss
129970    france  ...                          Domaine Schoffit

[129971 rows x 13 columns]
```

Note: need to use `str(row.country)` because some of the rows have
"NaN" for the country!


## grouping

Create groups of reviews with same "points" value,
thenfind minimum price in each group:

```
>>> reviews.groupby('points').price.min()
points
80      5.0
81      5.0
82      4.0
83      4.0
84      4.0
85      4.0
86      4.0
87      5.0
88      6.0
89      7.0
90      8.0
91      7.0
92     11.0
93     12.0
94     13.0
95     20.0
96     20.0
97     35.0
98     50.0
99     44.0
100    80.0
Name: price, dtype: float64
```

Most expensive wine from each winery:

```
>>> reviews.groupby('winery').price.max()
winery
1+1=3                  20.0
10 Knots               35.0
100 Percent Wine       18.0
1000 Stories           19.0
1070 Green             25.0
                       ...
Órale                  30.0
Öko                    11.0
Ökonomierat Rebholz    90.0
àMaurice               65.0
Štoka                  23.0
Name: price, Length: 16757, dtype: float64
```

or multiple stats for each winery:

```
>>> reviews.groupby('winery').price.agg([len, min, max])
                      len   min   max
winery
1+1=3                 6.0  16.0  20.0
10 Knots              4.0  21.0  35.0
100 Percent Wine      3.0  18.0  18.0
1000 Stories          2.0  19.0  19.0
1070 Green            1.0  25.0  25.0
...                   ...   ...   ...
Órale                 1.0  30.0  30.0
Öko                   2.0  11.0  11.0
Ökonomierat Rebholz   4.0  45.0  90.0
àMaurice             40.0  18.0  65.0
Štoka                 3.0  20.0  23.0

[16757 rows x 3 columns]

```

## missing data

```
>>> reviews[pd.isnull(reviews.country)]
       country  ...                           winery
913        NaN  ...               Gotsa Family Wines
3131       NaN  ...                Barton & Guestier
4243       NaN  ...  Kakhetia Traditional Winemaking
9509       NaN  ...                         Tsililis
9750       NaN  ...                         Ross-idi
...        ...  ...                              ...
124176     NaN  ...                Les Frères Dutruy
129407     NaN  ...                      El Capricho
129408     NaN  ...                      El Capricho
129590     NaN  ...                        Büyülübağ
129900     NaN  ...                           Psagot

[63 rows x 13 columns]
```

Change these to "Unknown":

```
>>> def fix(row):
...    if pd.isnull(row.country):
...       row.country = "Unknown"
...    return row
...
>>> new = reviews.apply(fix, axis='columns')
>>> new[pd.isnull(new.country)]
Empty DataFrame
Columns: [country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery]
Index: []
```


## answer questions...

How many of each variety?

```
>>> reviews.variety.value_counts()
Pinot Noir                   13272
Chardonnay                   11753
Cabernet Sauvignon            9472
Red Blend                     8946
Bordeaux-style Red Blend      6915
                             ...
Pinotage-Merlot                  1
Loureiro-Arinto                  1
Aidani                           1
Xinisteri                        1
Sauvignon Blanc-Assyrtiko        1
Name: variety, Length: 707, dtype: int64
```

How many highly-rated wines does each country have?

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

The above looks terrible, but here's what it does:

- grab only rows with points greater than or equal to 94
- sort those wines by points (`sort_values(by='points'...)`)
- grab all rows, just the columns we want (`.loc[:, cols]`)
- group those by country and count how many of each country
- then finally sort the results of all of that...


