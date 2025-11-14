import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# collection of account numbers for locating each data set
googleAccount = "600-613-00"
appleAccount = "499-130-00"
microsoftAccount = "312-003-50"
amazonAccount = "434-502-00"
toyotaAccount = "707-074-44"

# used for the for loop at the end for the main executable
totalCompanies = ["Google", "Apple", "Microsoft", "Amazon", "Toyota"]

starterDataFrame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")
starterDataFrame = starterDataFrame.fillna("")

# this method gathers the specific account data for each company, and imports it into a list.
def gatherAccountData(company):
    accountData = []
    for index, row in starterDataFrame.iterrows(): # for each row, determine what company it is and if the account number matches.
        if row['rewards_number'] == googleAccount and company == "Google":
            accountData.append(index)
        elif row['rewards_number'] == appleAccount and company == "Apple":
            accountData.append(index)
        elif row['rewards_number'] == microsoftAccount and company == "Microsoft":
            accountData.append(index)
        elif row['rewards_number'] == amazonAccount and company == "Amazon":
            accountData.append(index)
        elif row['rewards_number'] == toyotaAccount and company == "Toyota":
            accountData.append(index)
    print({company}, "data has been located.")
    return accountData

# this method locates the average spending for each company based upon the data set.
# takes in the company name, and the data index list for that company.
# this makes it more efficient by already knowing what rows it needs to aim for.
def analyzeSpending(company, data):
    amount = 0
    transactions = len(data)
    for items in data:
        curAmount = starterDataFrame.iloc[items]['order_amt'] # the curAmount contains a '$' sign

        amount += float(curAmount.replace('$', ''))
    print({company}, "spending analyzed")
    return amount / transactions # gets the average

# this method determines the average amount of discounts applied. Does not take into account orders that did not have discounts as that would ruin the results.
def analyzeDiscounts(company, data):
    amount = 0
    count = 0

    for items in data:
        curAmount = starterDataFrame.iloc[items]['discount_amt']
        if not curAmount == '':
            amount += float(curAmount)
            count += 1

    if count > 0:
        amount = amount / count
    return amount

# y axis revenue, x axis frequency of purchases
def analyzeFrequency(company, data):
    x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y = [] # we need to determine the average revenue per month, and these must align with the above list.

    date = [] # what is the current date for this transaction?
    amount = [] # what was the transaction amount?
    for items in data: # gathers up the date and amount per transaction and places them in a list
        cur_date = starterDataFrame.iloc[items]["transaction_date"]
        curAmount = starterDataFrame.iloc[items]['order_amt']

        n_date = cur_date.split('-')
        date.append(int(n_date[1]))
        amount.append(float(curAmount.replace('$', '')))
    
    for month in range(1, 13): # for each month in the graph, determine the average spending
        averageForMonth = 0
        countForMonth = 0
        for dates in date: # for the dates, determine if it is within the month specficied, and then collect all of its transactions
            if dates == month:
                countForMonth += 1
                averageForMonth += amount[date.index(dates)]
        averageForMonth = averageForMonth / countForMonth
        y.append(averageForMonth) # once the average spending is well averaged, append to the y list for this month
    
    # this creates each graph
    plt.plot(x, y)
    plt.title(f"{company} Monthly Spending Frequency")
    plt.xlabel("Month")
    plt.ylabel("Average Spending ($)")
    plt.show()
    print({company}, "frequency completed.")

# main executable
for company in totalCompanies:
    accountData = gatherAccountData(company)
    avgSpending = analyzeSpending(company, accountData)
    print("The Average spending for", company, "is: $", avgSpending)

    avgDiscounts = analyzeDiscounts(company, accountData)
    print("The average discounts applied for", {company}, "is: $", avgDiscounts)
    analyzeFrequency(company, accountData)
print("Spending Frequency and Averages completed.")
