import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the main DataFrame
raw_data = pd.read_csv("./hackathon/HackathonDataset.csv")

# Fill all empty values with "", for easier sorting
filled_data = raw_data.fillna("")

# List of all states where transactions occur
states_list = ["Alabama", "California", "Florida", "Georgia", "Mississippi", "South Carolina","Texas", "Washington"]

# declare a data list to hold states, transactions, and revenues
data_list = []

for state in states_list:
    # create a data frame holding transaction from a state
    state_frame = filled_data.loc[(filled_data["location_state"] == f"{state}"),["location_state", "order_amt"]]
    
    # grab the number of transactions
    frequency = len(state_frame)

    # sum along the "order_amt" column to get the revenue
    revenue = (state_frame['order_amt'].str[1:]).astype(float).sum()
    state_vals = [state, frequency, revenue]

    # Add the values to a list to convert into a dataframe later
    data_list.append(state_vals)


# only creates the graph when run directly
if __name__ == "__main__":
    # Use MatPlotLib to create the double bar graph
    list_labels = "state", "transactions", "revenue"
    new_frame = pd.DataFrame(data_list, columns= list_labels)

    fig = plt.figure()

    ax = fig.add_subplot(111)
    ax2 = ax.twinx()

    width = 0.4

    new_frame.transactions.plot(kind = 'bar', color = 'blue', ax = ax, width = width, position = 1)
    new_frame.revenue.plot(kind = "bar", color = 'red', ax = ax2, width = width, position = 0)

    ax.set_ylabel('Transactions')
    ax2.set_ylabel('Revenue')
    plt.xlabel("State")

    state_abbr_list = ["AL","CA","FL","GA","MS", "SC", "TX", "WA"]

    plt.xticks([0,1,2,3,4,5,6,7], state_abbr_list)

    plt.title("Revenue and Transactions per State")

    plt.show()