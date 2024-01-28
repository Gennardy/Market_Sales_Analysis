import pandas as pd

market = pd.read_csv("D:\Data Analyst\Project\supermarket_sales - Sheet.csv")

#Check for a null value
# print(market.isnull().sum())

#Check for duplicate values
market.drop_duplicates(inplace=True)

#Change the Date column to datetime format
market['Date'] = pd.to_datetime(market['Date'])
market['Date'].strftime("%m-%y")


#Check the formatting
market['City'] = market['City'].str.upper()

#Change gross margin percentage column format to %
market['gross margin percentage'] = market['gross margin percentage'].apply(lambda x: f'{x *1:.6f}%')

print(market.head(10))

#Save the cleaned dataset
#market.to_csv("D:\Data Analyst\Project\supermarket_sales - Sheet(Cleaned).csv", index=False)