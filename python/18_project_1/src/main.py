import pandas as pd

df = pd.read_csv("data/expenses.csv")

# print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.describe())
# print(df[["date", "amount"]])
# print("SUM: ",df["amount"].sum())
# print("MAX: ",df["amount"].max())
# print("MIN: ",df["amount"].min())
# print("MEAN: ",df["amount"].mean())
# print("STD: ",df["amount"].std())
# large_expenses = df[df["amount"] > 500]
# print(large_expenses)
# food = df[df["category"] == "Food"]
# print(food)
# result = df[
#     (df["category"] == "Food") &
#     (df["amount"] > 300)
# ]
# print(result)

# import numpy as np
# amounts = df["amount"].to_numpy()
# print(amounts)
# print(np.mean(amounts), df["amount"].mean())
# print(np.median(amounts), df["amount"].median())
# print(np.std(amounts), df["amount"].std())
# print(np.min(amounts), df["amount"].min())
# print(np.max(amounts), df["amount"].max())
# print(np.sum(amounts), df["amount"].sum())

# print(df)
# print(df.groupby("category").sum()["amount"])

