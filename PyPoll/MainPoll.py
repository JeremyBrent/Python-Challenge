#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csvpath = os.path.join('Resources', 'election_data.csv')


# In[3]:


totalvotes = 0
candidates = []
khanvotes = 0
correyvotes = 0
livotes = 0 
toolvotes = 0

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    #print(csvheader)
    for row in csvreader:
        #Count the total votes casted
        totalvotes += 1
        #Create a list of all the candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            #print(candidates)
        #Khan votes   
        if row[2] == "Khan":
            khanvotes += 1
            percentagekhan = khanvotes / totalvotes
        #Correy votes
        elif row[2] == "Correy":
            correyvotes += 1
            percentagecorrey = correyvotes / totalvotes
        #Li votes
        elif row[2] == "Li":
            livotes += 1
            percentageli = livotes / totalvotes
        #O'Tooley votes
        else:
            toolvotes += 1
            percentagetool = toolvotes / totalvotes
        
#If Khan wins           
if khanvotes > correyvotes and correyvotes > livotes and livotes > toolvotes:
    winner = "Khan"
#If Correy wins
elif correyvotes > khanvotes and khanvotes > livotes and livotes > toolvotes:
    winner = "Correy"
#If Li Wins
elif livotes > khanvotes and khanvotes > correyvotes and correyvotes > toolvotes:
    winner = "Li"
#If O'Tooley wins
else:
    winner = "O'Tooley"

output = open("Output.txt", "w")
output.write(f"Election Results \n------------------------- \nTotal Votes: {totalvotes:,} \n------------------------- \nKhan: {percentagekhan:.2%}({khanvotes:,}) \nCorrey: {percentagecorrey:.2%}({correyvotes:,}) \nLi: {percentageli:.2%}({livotes:,}) \nO'Tooley: {percentagetool:.2%}({toolvotes:,}) \n------------------------- \nWinner: {winner} \n-------------------------")
output.close()


# In[4]:


print("Election Results")
print("-------------------------")
print(f'Total Votes: {totalvotes:,}')
print("-------------------------")
print(f'Khan: {percentagekhan:.2%}({khanvotes:,})')
print(f'Correy: {percentagecorrey:.2%}({correyvotes:,})')
print(f'Li: {percentageli:.2%}({livotes:,})')
print(f"O'Tooley: {percentagetool:.2%}({toolvotes:,})")
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")


# In[ ]:




