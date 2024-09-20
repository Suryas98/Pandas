""
import pandas

mydataset = {
    'cars':["BMW","Volvo","Ford"],
    'passings' : [3,7,2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

# PANDAS AS PD

import pandas as pd

mydataset = {
    'cars':["BMW","Volvo","Ford"],
    'passings' : [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)     

# Pandas Version

import pandas as pd
print(pd.__version__)    

# PANDAS SERIES

import pandas as pd
a=[1,7,2]
myvar = pd.Series(a)

print(myvar)
print(myvar[0])  

#Create Labels

import pandas as pd
a=[1,7,2]
myvar = pd.Series(a, index = ["x","y","z"])

print(myvar)
print(myvar["y"])  

# Key/Value Object as Series

import pandas as pd
calories = {"day1" : 420,"day2" : 380,"day3" : 390}
myvar = pd.Series(calories)
print(myvar)  

# Key/Value Object as Series create day1 and day2

import pandas as pd
calories = {"day1" : 420,"day2" : 380,"day3" : 390}
myvar = pd.Series(calories, index = ["day1","day2"])
print(myvar)  

# Data Frames two Series

import pandas as pd

data = {
    "calories" : [420, 380, 390],
    "duration" : [50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar) 

import pandas as pd

data = {
    "calories" : [420, 380, 390],
    "duration" : [50,40,45]
}
df = pd.DataFrame(data)
print(df)

# JSON file into DataFrame

import pandas as pd

df = pd.read_json('data.json')
print(df.to_string()) 

#Dictionary as JSON

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)  







