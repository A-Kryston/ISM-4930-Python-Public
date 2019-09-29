#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 1 - Nested Conditionals (2 of 2)
# September 29, 2019

# This program determines level of Expertise based on an exam score, where
# 95-100 is Expert Level
# 80- 94 is Proficient Level
# 70- 79 is Competent Level
#  0- 69 is Beginner Level

score = int(input('Enter exam score (integers between 0 to 100): '))  # Score variable captures input value for exam score

if score >= 70:           # Initial if conditional statement for the score (testing for 70 and above)
    if score >= 80:       # 1st nested if conditional statement for the score (testing for 80 and above)
        if score >= 95:   # 2nd nested if conditional statement for the score (testing for 95 and above)
            print (('Expert Level (Score ='), score ,')')     # Indicates level of Expertise and the score
        else:             # If 2nd nested if statement is false, this else becomes active
            print (('Proficient Level (Score ='), score ,')') # Indicates Level of Expertise and the score
    else:                 # If 1st nested if statement is false, this else becomes active
        print (('Competent Level (Score ='), score , ')')     # Indicates Level of Expertise and the score
else:                     # If the initial if statement is false, this else becomes active
    print (('Beginner Level (Score ='), score , ')')          # Indicates level of Expertise and the score

