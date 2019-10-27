#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 2 - Functions and Iterations 
# October 27, 2019

### Solving business problem #1 using a function ###

# This program calculates the sale price of an item.
# The original price is input by the user, 
# then the system calculates the sale price.
# The program then shows the original price and the sale price. 

def sale_calc():                                                    # Define function called sale_calc (sale calculator)
    print ("Enter product price (do not include a dollar sign): ")  # Request product price to be entered by the user
    orig_price = float(input())                                     # Original price variable assigned from user input
    sale_pct = .25                                                  # Sale percentage variable assigned as 25%
    sale_price = orig_price - (orig_price*sale_pct)                 # Formula calculates the sale price
    print (("Original Price: "), orig_price, ("dollars"))           # Shows the original price
    print (("Sale Price: "), round(sale_price,2), ("dollars"))      # Shows the calculated sale price
    
sale_calc()                                                         # Call 'sale_calc' function


# In[ ]:



### Solving business problem #1 using iteration ###

# The program calculates the sale price of an item.
# The original price is provided from a list.

product_price = [35.00, 60.00, 100.00]                           # Associates product_price variable with list of prices
for orig_price in product_price:                                 # Sets up 'for loop' to iterate through product prices list
    sale_pct = .25                                               # Sale percentage assigned as 25% 
    sale_price = orig_price - (orig_price*sale_pct)              # Formula calculates the sale price
    print (("The original price is"), orig_price, ('dollars;'),  # Shows the original price and
    ("the sale price is"), round(sale_price,2), ('dollars.'))    # shows the calculated sale price
    


# In[ ]:



### Solving business problem #2 using a function ###

# This program displays a thank you message to the customer.
# The function could be reused to display the message on order confirmations, bill of lading, invoices, etc.

def thank_cust ():                                             # Define function called 'thank_cust'
    customer = "Sue Jones"                                     # Associates customer variable to 'Sue Jones'
    print (customer, '~', 'Thank you for shopping with us!')   # Shows thank you message
    
thank_cust()                                                   # Calls 'thank_cust' function


# In[ ]:


### Solving business problem #2 using iteration ###

# This program displays a thank you message to the customer.
# The customer name is provided from a list of names.

customer = ['Anna Wells','Jose Fernandez','Jenny Green']   # Associates customer variable with list of names
for name in customer:                                      # Sets up 'for loop' to iterate through customer list
    print (name,'~ Thank you for shopping with us!')       # Shows the thank you message

