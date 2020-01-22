import pandas as pd

sr = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'],['Yellow']])
print(sr)
brr = sr.apply(pd.Series) #.stack().reset_index(drop=True)
print(brr)
print(type(brr))