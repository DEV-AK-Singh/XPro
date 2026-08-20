# import matplotlib.pyplot as plt
# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [120, 150, 180, 140]
# plt.plot(months, sales)
# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("expenses.csv")
df.plot(x="date", y="amount", kind="line")
plt.title("Expenses")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.show()
