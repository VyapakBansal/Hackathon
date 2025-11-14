import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## collection of account numbers for locating each data set
googleAccount = 600-613-00
appleAccount = 499-130-00
microsoftAccount = 312-003-50
amazonAccount = 434-502-00
toyotaAccount = 707-074-44

starterDataFrame = pd.read_csv("./Pandas Hackathon Files/HackathonDataset.csv")
sorted = starterDataFrame.sort_values(['rewards_number'])

print(sorted)
