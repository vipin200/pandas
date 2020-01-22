import pandas as pd

df = pd.DataFrame([[0 ,1 ,4 ,7],[1 ,2 ,5 ,5],[2 ,3, 6, 8],[3, 4, 9, 12],[4, 7 ,5 ,1],[5 ,11 ,0 ,11]], columns=list("ABCD") )
print(df)
arr = pd.Series(df['A'])
print(arr)


