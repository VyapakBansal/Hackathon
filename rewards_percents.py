import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the main DataFrame
raw_data = pd.read_csv("./hackathon/HackathonDataset.csv")

# Fill all empty values with "", for easier sorting
filled_data = raw_data.fillna("")

# Use .loc[] to filter all values with a rewards number
transactions_with_rewards_number = filled_data.loc[filled_data["rewards_number"] != "", ["rewards_number"]]
transactions_with_both = filled_data.loc[(filled_data["rewards_number"] != "") & filled_data["rewards_member"], ["rewards_number"]]

# Filter duplicate account numbers
unique_users_with_rewards_number = transactions_with_rewards_number.drop_duplicates()
unique_users_with_both = transactions_with_both.drop_duplicates()


# Divide the number of accounts by the number of total trans
percentage_with_rewards_number = (len(unique_users_with_rewards_number) / len(raw_data))
percentage_with_both = len(unique_users_with_both) / len(filled_data)

# create the labels and data for the pie chart
labels = "No Account", "Account w/o\nMembership", "Accounts w/\nMembership"
sizes = [1-percentage_with_rewards_number, percentage_with_rewards_number - percentage_with_both, percentage_with_both]

# plot them onto the screen
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct = "%1.2f%%") 

# create a title
plt.title("Account & Membership Percentages")

# show the graph
plt.show()
