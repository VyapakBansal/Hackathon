import pandas as pd
import numpy as np
# Read and store the csv
data_frame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")

#
data_frame = data_frame.sort_values('transaction_date')
# Convert each entry into a float without "$"
order_amount_frame = (data_frame['order_amt'].str[1:]).astype(float)
# Sum the values
total_sales = order_amount_frame.sum()

# Find average revenue per transaction
average_transaction = order_amount_frame.mean()

#Graphing the consecutive revenue
consecutive_revinue = order_amount_frame.cumsum()


data_frame = pd.concat([pd.to_datetime(data_frame['transaction_date']),consecutive_revinue/1000000], axis=1)



data_frame.plot(title='Revenue over Time', x='transaction_date', y='order_amt', legend=False)
plt.ylabel('Total Revenue(in millions of dollars)')
plt.xlabel('Date')
plt.show()