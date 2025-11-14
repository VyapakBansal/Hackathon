import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


starterDataFrame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")
print(f"Maxing our transaction hours at {starterDataFrame['transaction_hour'].value_counts().index[0]}")
starterDataFrame["transaction_hour"] = pd.to_datetime(starterDataFrame["transaction_hour"])
# starterDataFrame["hour_only"] = starterDataFrame["transaction_hour"].dt.floor("h")
# hour_counts = starterDataFrame["hour_only"].value_counts().sort_index()
# plt.plot(hour_counts.index, hour_counts.values)
# plt.xlabel("Hour")
# plt.ylabel("Transactions")
# plt.show()
starterDataFrame["year_month"] = starterDataFrame["transaction_hour"].dt.to_period("M")
monthly_revenue = starterDataFrame.groupby("year_month")["order_amt"].sum()

print(type(monthly_revenue))