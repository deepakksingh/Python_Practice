import pandas as pd
import numpy as np

fruits = ['apples','oranges','cherries']
quantities = [10,20,30]
prices = [10,10,20]

fruits_qty = pd.Series(quantities, index=fruits)
fruits_rates = pd.Series(prices,index=fruits)

print(fruits_qty)
print(fruits_rates)

fruits_prices = fruits_qty*fruits_rates
print(fruits_prices)
print(f"total cost: {sum(fruits_prices)}")

fruits_2 = ["pear","raspberry"]
fruits_2_qty = [100,200]
fruits_2_rates = [200,100]

fruits_2_qty = pd.Series(fruits_2_qty, index=fruits_2)
fruits_2_rates = pd.Series(fruits_2_rates, index= fruits_2)
print(fruits_2_qty)
print(fruits_2_rates)

fruits = fruits_qty.append(fruits_2_qty)


print(fruits[['apples','pear']])

fruits*2+3

fruits.apply(np.log)

fruits.apply(lambda x : x if x > 50 else x+50)
fruits[fruits>=100]

print("apples" in fruits)

cities = {"London":    8615246, 
          "Berlin":    3562166, 
          "Madrid":    3165235, 
          "Rome":      2874038, 
          "Paris":     2273305, 
          "Vienna":    1805681, 
          "Bucharest": 1803425, 
          "Hamburg":   1760433,
          "Budapest":  1754000,
          "Warsaw":    1740119,
          "Barcelona": 1602386,
          "Munich":    1493900,
          "Milan":     1350680}

city_series = pd.Series(cities)
print(city_series)
print(sum(city_series))
print(city_series)

my_cities = ['London','Bangalore','Munich']