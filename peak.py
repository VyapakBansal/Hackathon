import pandas as pd

starterDataFrame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")
sorted = starterDataFrame.sort_values(["transaction_hour"], ascending=True)
print(sorted.head(50))