import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Do more restaurants provide online delivery compared to offline services?
# Which types of restaurants are most favored by the general public?
# What price range do couples prefer for dining out?

plt.cla()

dataframe = pd.read_csv("projects/Zomato/Zomato-data-.csv")
# print(dataframe.head(5))

# Step 3: Data Cleaning and Preparation
# 1. Convert the rate column to a float by removing denominator characters.

def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)

# print(dataframe.head(5))

# 2. Getting summary of the dataframe use df.info().

# dataframe.info()

# 3. Checking for missing or null values to identify any data gaps.

# print(dataframe.isnull().sum())

# Step 4: Exploring Restaurant Types

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
# plt.show()

# plt.cla()
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('Votes')

# plt.show()


# Step 5: Identify the Most Voted Restaurant

plt.cla() # Clear the current axes
max_votes = dataframe['votes'].max()
restaurant_with_max_votes=dataframe.loc[dataframe['votes']==max_votes,'name']
# print('Restaurant(s) with the maximum votes:')
# print(restaurant_with_max_votes)


sns.countplot(x=dataframe['online_order'])
# plt.show()

# Step 7: Analyze Ratings
# plt.cla()
plt.hist(dataframe['rate'],bins=5)
plt.title('Rating Distribution')
# plt.show()

# Step 8: Approximate Cost for Couples
couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

# plt.show()

# Step 9: Ratings Comparison - Online vs Offline Orders
plt.cla()
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)
# plt.show()

# Step 10: Order Mode Preferences by Restaurant Type
plt.cla()
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()

print("last line")