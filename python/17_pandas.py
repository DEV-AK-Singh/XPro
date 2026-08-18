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

## PANDAS CSV FILES
# student_A = {"name": "abhishek", "age": 24, "score": 85}
# student_B = {"name": "bob", "age": 24, "score": 85}
# student_C = {"name": "charlie", "age": 24, "score": 85}
# df = pd.DataFrame([student_A, student_B, student_C])
# df.to_csv("students.csv", index=False)

## READING CSV
# df = pd.read_csv("data.csv")
# df = pd.read_csv("data.csv", index_col="Date", nrows=3, usecols=["Pulse", "Calories", "Duration", "Date"], skiprows=[1, 2, 3])
# df = pd.read_csv("data.csv", header=2, nrows=5)
# df = pd.read_csv("data.csv", nrows=3, names=["Date-X", "Pulse-X", "Calories-X", "Duration-X"], skiprows=[0])
# df = pd.read_csv("data.csv", nrows=5, header=None)
# df = pd.read_csv("data.csv", dtype={"Date": str, "Pulse": float, "Duration": float})
# print(df)