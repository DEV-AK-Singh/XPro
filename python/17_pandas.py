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

## PANDAS FUNCTIONS
# df = pd.read_csv("data.csv")
# print(df)  
# print(df.head(10)) # first 10 rows
# print(df.tail(10)) # last 10 rows
# print(df.describe())  # summary
# print(df.info())  # information
# print(df.isnull())  # true or false
# print(df.isnull().sum()) # missing values
# print(df["Date"].value_counts()) # frequency
# print(df["Date"].unique()) # unique values
# print(df["Date"].nunique()) # number of unique values
# print(df["Date"].value_counts(dropna=False)) # frequency with missing values
# print(df["Date"].value_counts(dropna=False, normalize=True)) # frequency with missing values in percentage
# print(df.sort_index(ascending=False, axis=1)) # sort columns by index (ascending, descending)
# print(df.sort_values("Date", ascending=False)) # sort rows by column (ascending, descending)
# print(df.sort_values(["Date", "Pulse"], ascending=[False, True])) # sort rows by multiple columns first by Date in descending order and then by Pulse in ascending order
# df.loc[df["Pulse"] < 100, ["Date", "Pulse"]] = [None, None] # replace values less than 100 with None in Date and Pulse columns
# df.iloc[df["Pulse"] < 100, 1:3] = [None, None] # replace values less than 100 with None in Date and Pulse columns
# difference between loc and iloc is that loc is used to select rows and columns by label, while iloc is used to select rows and columns by integer location
# print(df)

## HANDLING MISSING DATA (DROPNA, FILLNA)
# df = pd.read_csv("data.csv")
# print(df)
# print(df.dropna()) # drop rows with missing values
# print(df.dropna(axis=1)) # drop columns with missing values
# print(df.dropna(how="all")) # drop rows with all missing values
# print(df.dropna(how="any")) # drop rows with any missing values
# print(df.dropna(subset=["Date"])) # drop rows with missing values in Date column
# print(df.dropna(subset=["Date", "Pulse"])) # drop rows with missing values in Date and Pulse columns
# print(df.fillna(0)) # fill missing values with 0
# print(df.fillna(df.mean(numeric_only=True)))
# print(df["Pulse"].fillna(df["Pulse"].mean()))
# print(df.ffill()) # fill missing values with previous value
# print(df.bfill()) # fill missing values with next value

## HANDLING MISSING DATA (REPLACE, INTERPOLATE)
# df = pd.read_csv("data.csv")
# print(df) 
# print(df.replace(100, 1)) # replace 0 with 1
# print(df.replace("[A-Za-z0-9]", "1", regex=True))
# print(df.replace([0, 1], [1, 2])) # replace 0 with 1 and 1 with 2
# print(df.replace({"Pulse": 0}, 1)) # replace 0 in Pulse column with 1
# print(df.replace({"Pulse": [0, 1]}, {0: 1, 1: 2})) # replace 0 and 1 in Pulse column with 1 and 2 
## Interpolate : fill missing values with previous or next value 
# num_cols = df.select_dtypes(include='number').columns 
# df[num_cols] = df[num_cols].interpolate(method='linear', limit_direction='both', axis=0)  
# print(df)

## MERGE AND CONCAT 
# df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
# df2 = pd.DataFrame({"A": [1, 2, 4], "D": [13, 14, 15], "E": [16, 17, 18]})
# print(df1)
# print(df2)
# print(pd.merge(df1, df2, on="A"))
# print(pd.merge(df1, df2, how="left", on="A"))
# print(pd.merge(df1, df2, how="right", on="A"))
# print(pd.merge(df1, df2, how="outer", on="A"))
# print(pd.merge(df1, df2, how="inner", on="A")) 
# print(pd.merge(df1, df2, left_index=True, right_index=True, suffixes=("_left", "_right")))
# df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
# df2 = pd.DataFrame({"D": [10, 11, 12], "E": [13, 14, 15], "F": [16, 17, 18]})
# df3 = pd.DataFrame({"G": [19, 20, 21], "H": [22, 23, 24], "I": [25, 26, 27]})
# print(df1)
# print(df2)
# print(df3)
# print(pd.concat([df1, df2, df3], axis=1))
# print(pd.concat([df1, df2, df3], axis=0))
# print(pd.concat([df1, df2, df3], axis=0, keys=["df1", "df2", "df3"]))
# print(pd.concat([df1, df2, df3], axis=0, keys=["df1", "df2", "df3"], join="inner"))