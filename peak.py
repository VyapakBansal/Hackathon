import pandas as pd
import matplotlib.pyplot as plt

# Initializing my dataframe
starterDataFrame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")
# Finding max transations done at a point.
max_transactions = starterDataFrame['transaction_hour'].value_counts().index[0]
print(f"Maximum transaction occurs at: {max_transactions}")
# Converting my transaction hours to a date time data structure
starterDataFrame["transaction_hour"] = pd.to_datetime(starterDataFrame["transaction_hour"])
# Rounding down the time stamps to fit in an hour frame.
starterDataFrame["hour_only"] = starterDataFrame["transaction_hour"].dt.floor("H")
# Sorting after counting all the hour frames.
hour_counts = (starterDataFrame["hour_only"].value_counts().sort_index())

# Plotting the graph using matplotlib
plt.plot(hour_counts.index, hour_counts.values)
plt.xlabel("Hour")
plt.ylabel("Transactions")
plt.show()
# Converting my transaction date to a date time data structure.
starterDataFrame["transaction_date"] = pd.to_datetime(starterDataFrame["transaction_date"])
# Coneverting all my dates to a year-month format.
starterDataFrame["year_month"] = starterDataFrame["transaction_date"].dt.to_period("M")
# Removing the dollar sign and making it a float value.
starterDataFrame["order_amt"] = (starterDataFrame["order_amt"].str[1:]).astype(float)
# Taking a sum of all the revenue by grouping them all together.
monthly_revenue = starterDataFrame.groupby("year_month")["order_amt"].sum()

# Plotting the graph using matplotlib
plt.bar(monthly_revenue.index.astype(str), monthly_revenue.values)
plt.xlabel("Month (YYYY-MM)")
plt.ylabel("Total Revenue ($)")
plt.title("Revenue per Month")
plt.show()
