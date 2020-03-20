#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import csv


# In[2]:


csvpath = os.path.join('Resources', 'budget_data.csv')


# In[3]:


months = 0
totalprofitsloss = 0
maxprofit = 0
minprofit = 0
previousrevenue = 0
revenuechangelist = []

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    for row in csvreader:
        #finding total months
        months += 1
        #finding the net profit/loss
        totalprofitsloss += int(row[1])
        #finding greatest increase in revenue
        if int(row[1]) > maxprofit:
            maxprofit = int(row[1]) - previousrevenue
            maxmonth = row[0]
        #finding min profit
        if int(row[1]) < minprofit:
            minprofit = int(row[1]) - previousrevenue
            minmonth = row[0]
        #finding the average revenue change 
        revenuechange = int(row[1]) - previousrevenue
        previousrevenue = int(row[1])
        revenuechangelist += [revenuechange]
    #popping first index with a value of row[1] from first row     
    revenuechangelist.pop(0)
    #finding the average revenue change 
    revenueaverage = sum(revenuechangelist) / len(revenuechangelist)
    
output = open('output.txt', 'w')

output.write(f'Financial Analysis \n---------------------------- \nTotal Months: {months} \nTotal Profit/Loss: ${totalprofitsloss:,} \nAverage Change: ${revenueaverage:,.6} \nGreatest Increase in Profit: ({maxmonth}) ${maxprofit:,} \nGreatest Decrease in Profit: ({minmonth}) ${minprofit:,}')

output.close()


# In[4]:


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {months}')
print(f'Total Profit/Loss: ${totalprofitsloss:,}')
print(f'Average Change: ${revenueaverage:,.6}')
print(f'Greatest Increase in Profit: ({maxmonth}) ${maxprofit:,}')
print(f'Greatest Decrease in Profit: ({minmonth}) ${minprofit:,}')


# In[ ]:





# In[ ]:




