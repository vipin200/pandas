import pandas as pd

arr = pd.Series([0,100,200,"python",300.12,400])
brr = pd.to_numeric(arr , errors="coerce")
print(brr)
crr = pd.to_numeric(arr , errors="ignore")
print(crr)