import pandas as pd
import numpy as np
years = range(2014, 2018)
shop1 = pd.Series([2409.19,2941.23,6534.23,6432.34], index = years)
shop2 = pd.Series([2234.19,2924.23,6244.23,6234.34], index = years)

row_wise_concat = pd.concat([shop1,shop2])
shop_df = pd.concat([shop1, shop2], axis=1)

print(row_wise_concat)
cities = ["Bangalore", "Hyderabad"]
shop_df.columns = cities

print(shop_df)
'''
We can create dataframes from dictionaries also
'''
cities = {"name": ["London", "Berlin", "Madrid", "Rome",
                   "Paris", "Vienna", "Bucharest", "Hamburg",
                   "Budapest", "Warsaw", "Barcelona",
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania",
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"]}

city_frame = pd.DataFrame(cities)
print(city_frame)
print(city_frame.columns.values)

print(city_frame["population"])

'''
By default dataframe is allocated the index values 0..etcetera
We can change it by using the index property
'''
ordinals = ["first", "second", "third", "fourth",
            "fifth", "sixth", "seventh", "eigth",
            "ninth", "tenth", "eleventh", "twelvth",
            "thirteenth"]
city_frame = pd.DataFrame(cities, index = ordinals)
print(city_frame)

'''
We can rearrange the order of the columns while creating the DataFrame
'''
city_frame = pd.DataFrame(cities, columns = ['name','country','population'], index = ordinals)
print(city_frame)

np.random.shuffle(ordinals)
print(ordinals)

city_frame = city_frame.reindex(index = ordinals)
print(city_frame)

'''
We can create the values associated in the dataframe as a key
'''
city_frame = pd.DataFrame(cities,
                columns = ["name","population"],
                index = cities['country'])
print(city_frame)
print(city_frame)

#we can also set the index after creating the DataFrame
city_frame = pd.DataFrame(cities)
city_frame = city_frame.set_index('country')
print(city_frame)

#we can also set the index after creating the DataFrame and also make it in-place
city_frame = pd.DataFrame(cities)
print(city_frame)
city_frame.set_index("country",inplace=True)
print(city_frame)
