#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 1 - Iterations, While Loop
# September 29, 2019

# Use while loop to calculate savings of 52 weekly deposits of $20 each (into a non-interest bearing account).

dep = 20       # Variable 'dep' represents the dollar amount being deposited weekly
week = 1       # Iteration variable 'week' represents the week of the deposit, beginning with week 1
savings = 0    # Variable 'savings' initiated with a value of 0. The code worked without establishing this variable
               # before the loop, but I like having all of the variables noted here and hope this preference is acceptable.

while week < 53:         # While condition statement (need 52 weeks only); this ensures the loop will eventually be false
    savings = dep*week   # Calculates the total savings
    print (('Your total savings as of week ') , week , (' is ') , savings, ' dollars')  # Confirms the loop is working
    week = week + 1      # Iterates through the weeks until the loop condition fails
print ('Great job, Saver!')  # Encouraging the saver with a comment


# In[ ]:




