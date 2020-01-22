import pandas as pd
import numpy as np

t1 = pd.Series([2, 4, 6, 8, 10] )
t2 = pd.Series([1, 4, 5, 7, 9] )
print(t1)
print(t2)

print(t1 > t2)
print(t1 == t2)
