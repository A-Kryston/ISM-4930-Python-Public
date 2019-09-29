#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 1 - Nested Conditionals (1 of 2)
# September 29, 2019

# The program is used to regulate the air conditioner settings in an auditorium.

temp = int(input('Enter current temperature (in Fehrenheit degrees): '))   # Input to get current temperature;
# In actuality, the temperature would be read systematically, not manually, but this is just to illustrate the concept

if temp > 78:         # If conditional statement to see if temperature is too hot
    if temp > 90:     # Nested if conditional statement determines if system may be broken and not cooling properly
        print ('The air conditioner may be broken. Enter a service ticket.')  # Indicates status/action required
    else:             # If nested if conditional statement is false, this else becomes active
        print ('It is too hot. Adjust the air conditioner temperature downward.')  # Indicates status/action required
elif temp < 68:       # Elif conditional statement to see if temperature is too cold
    if temp < 60:     # Nested if conditional statement determines if system may be broken and cooling excessively
        print ('The air conditioner may be broken. Enter a service ticket.')  # Indicates status/action required
    else:             # If nested if conditional statement is false, this else becomes active
        print ('It is too cold. Adjust the air conditioner temperature upward.')  # Indicates status/action required
else:                 # Else becomes active if first if and elif statements are false
    print ('The temperature is comfortable. Do not adjust the air conditioner settings.')

