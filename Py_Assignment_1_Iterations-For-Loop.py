#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 1 - Iterations, For Loop
# September 29, 2019

# This script increases salaries for five of the top performing associates; 
# In reality, a much longer list of all employees' salaries could be used, which would be an even better use of the loop

for salary in [37250.00, 42500.00, 47000.00, 49300.00, 52000.00]:  # Sets up the 'for loop' with a finite number of values
    salary = salary*1.03                                           # Loop adds 3% to all salaries for top five performers
    print (('The new salary is'), salary ,('dollars'))             # Confirms iterations and calculations performed correctly

