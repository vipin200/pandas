import pandas as pd

arr = pd.Series([3,4,5,6])
brr = arr.tolist()
crr = arr.to_list
print(brr)
print(crr)
print(type(brr))
print(type(crr))