import pandas as pd
# using from a list
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)

# from numpy array
import numpy as np
np_array = np.array([1, 2, 3, 4])
series = pd.Series(np_array)
print(series)

# from dictionary
data = {'a': 1, 'b': 2, 'c': 3}
series = pd.Series(data)
print(series)

# accessing element of series
print(series[0])  # Access by integer index
print(series['a'])  # Access by label
# slicing series
print(series[:2])  # First two elements

# attribute and method of pandas series
series.index    #Returns the index of the Series.
series.values   #Returns the data of the Series as a NumPy array.
series.head(2)  #Returns the first n elements.
series.tail(2)  #Returns the last n elements.
series.mean()   #Calculates the mean of the Series (only for numeric data).

# custom index in series
data = [100, 200, 300]
index = ['a', 'b', 'c']
series = pd.Series(data, index=index)
print(series)




