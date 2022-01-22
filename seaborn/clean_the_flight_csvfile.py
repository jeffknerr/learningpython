"""
input: flight.csv
       data for 14 airlines, many flights, all in 2015
       https://www.kaggle.com/usdot/flight-delays?select=flights.csv
output: average airline delay per month

month airline1 airline2...airline 14
1     avgdelay avgdelay...avgdelay
2
3
,,,
11
12


use boring old python, since I don't know how to easily
do this in pandas (yet)

J. Knerr
Jan 2022
"""

import pandas as pd

# example data from file
"""
YEAR,MONTH,DAY,DAY_OF_WEEK,AIRLINE,FLIGHT_NUMBER,TAIL_NUMBER,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY,TAXI_OUT,WHEELS_OFF,SCHEDULED_TIME,ELAPSED_TIME,AIR_TIME,DISTANCE,WHEELS_ON,TAXI_IN,SCHEDULED_ARRIVAL,ARRIVAL_TIME,ARRIVAL_DELAY,DIVERTED,CANCELLED,CANCELLATION_REASON,AIR_SYSTEM_DELAY,SECURITY_DELAY,AIRLINE_DELAY,LATE_AIRCRAFT_DELAY,WEATHER_DELAY
2015,1,1,4,AS,98,N407AS,ANC,SEA,0005,2354,-11,21,0015,205,194,169,1448,0404,4,0430,0408,-22,0,0,,,,,,
2015,1,1,4,AA,2336,N3KUAA,LAX,PBI,0010,0002,-8,12,0014,280,279,263,2330,0737,4,0750,0741,-9,0,0,,,,,,
"""

# smaller file with 100,000 entries
datafile = "testflights.csv"
# real file with 5M entries
datafile = "flights.csv"
delays = pd.read_csv(datafile)

dc = delays.columns
for i in range(len(dc)):
    print(i, dc[i])
airlines = list(delays.AIRLINE.unique())
print(airlines)

# just pull out the arrival delays info
arrdel = delays.loc[:, ['YEAR', 'MONTH', 'DAY', 'AIRLINE', 'ARRIVAL_DELAY']]
print(arrdel.head())
print(arrdel.tail())

# now get the averages per month per airline
data = {}
for carrier in airlines:
    counts = [0]*12       # how many flights each month
    totals = [0]*12       # total minutes of delays each month
    data[carrier] = [counts, totals]
print(data)
for index, row in arrdel.iterrows():
    carrier = row[3]
    delay = float(row[4])
    month = int(row[1])
    # skip if delay is NaN
    if not pd.isna(delay) and month <= 12:
        data[carrier][0][month-1] += 1
        data[carrier][1][month-1] += delay
print(data)

# output the averages
summary = {}
for carrier in data:
    avgdelay = []
    for i in range(12):
        count = data[carrier][0][i]
        total = data[carrier][1][i]
        try:
            result = total/count
        except ZeroDivisionError:
            result = 0
        avgdelay.append(result)
    summary[carrier] = avgdelay

cleanDF = pd.DataFrame(summary)
months = list(range(1, 13))
cleanDF['MONTH'] = months
cleanDF.to_csv('clean_flights.csv', index=False)
