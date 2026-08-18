import pandas as pd

## SERIES
# x = pd.Series([1, 2, 3, 4, 5])
# print(x)
# y = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
# print(y)
# z = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
# print(z)
# a = pd.Series([1,2])
# b = pd.Series([4,5,6,7])
# c = a + b
# print(c)

## DATAFRAMES
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# d = [10,11,12]
# df = pd.DataFrame({"A": a, "B": b, "C": c, "D": d}, index=[1,2,3])
# print(df)
# print(df.columns)
# print(df.index)
# print(df.values)
# print(df.head(2))
# print(df.tail(2))
# print(df["A"][:2])
# print(df.loc[2]) # loc = location index
# print(df.iloc[2]) # iloc = integer location

## ARITHMETIC OPERATIONS
# df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6], "C": [7,8,9]}) 
# print(df)
# print("".center(50, "-"))
# df["SUM"] = df["A"] + df["B"] + df["C"]
# df["SUB"] = df["A"] - df["B"] - df["C"]
# df["MUL"] = df["A"] * df["B"] * df["C"]
# df["DIV"] = df["A"] / df["B"] / df["C"]
# df["AgtB"] = df["A"] > df["B"]
# df["AgtC"] = df["A"] > df["C"]
# print(df)

## INSERT & DELETE
# df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6], "C": [7,8,9]})
# print(df)
# print("".center(50, "-"))
# df.insert(1, "D", [10, 11, 12]) # df["D"] = [10, 11, 12]
# print(df)
# print("".center(50, "-"))
# del df["D"]
# print(df)