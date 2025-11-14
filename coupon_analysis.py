import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read and store the csv
data_frame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")

# Remove all rows without an entry in either column to filter out errors
data_frame = data_frame.dropna(subset =['discount_amt', 'coupon_flag'])

# Count the number of coupon flags and add the total discount amount
count = data_frame['coupon_flag'].count()
lost_revenue = data_frame['discount_amt'].sum()

# Find the real revenue from people who used coupons
revenue_from_coupons = ((data_frame['order_amt'].str[1:]).astype(float)).sum()
# Find the revenue if no coupons were used
unrealized_revenue = revenue_from_coupons + lost_revenue

# Create a data frame with the results
results = pd.DataFrame(data= {'Potential Revenue From Coupon Users':[unrealized_revenue/1000000], 'Real Revenue From Coupon Users':[revenue_from_coupons/1000000]})

# Make a graph
plot = results.plot.bar(title = 'Revenue Analysis from Coupon Users')
plt.axis([0,0,2.65,2.7])
plt.ylabel("Revenue(in millions of dollars)")
plt.xticks([])
plt.legend(loc='lower right')
plt.show()