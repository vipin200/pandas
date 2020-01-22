import pandas as pd
import numpy as np
# t1 = pd.Series([2, 4, 6, 8, 10] ,index=['A','B','C','D','E'])
# t2 = pd.Series([1, 3, 5, 7, 9],index=['C','A','X','D','E'] )
t1 = pd.Series([2, 4, 6, 8, 10] )
t2 = pd.Series([1, 3, 5, 7, 9] )
print(t1)
print(t2)

t3 = t1 + t2
print(t3)
t3 = t1 * t2
print(t3)
t3= t1 / t2
print(t3)

t3= t1-t2
print(t3)
