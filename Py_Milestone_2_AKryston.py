#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Milestone 2
# October 27, 2019

import pandas as pd
import numpy as np

Location = "Datasets/cities_health_data.csv"    # Identifies location of the csv file
df = pd.read_csv(Location)                      # Creates 'df' dataframe from data in csv file
df.head(3)                                      # Shows first three rows of the dataframe


# In[ ]:


df.shape                                        # Provides count of rows and columns in the dataframe


# In[ ]:


df.dtypes                                       # Provides data type for each column ('object' indicates 'string' data type)


# In[ ]:


df['Data_Value'].describe()         # Shows stats for 'data_value' column; count implies there are blanks in the column


# In[ ]:


df.dropna(subset=['Data_Value'],inplace=True)   # Removes all rows where Data_Value is blank
df.shape                                        # Provides updated count of rows and columns in the dataframe


# In[ ]:


indexNames = df[df['GeographicLevel'] == 'Census Tract'].index   # Identifies rows where GeographicLevel equals 'Census Tract'
df.drop(indexNames, inplace=True)                                # Removes all rows containing 'Census Tract'
df.shape                                                         # Shows updated count of rows and columns in the dataframe


# In[ ]:


df.drop(['GeographicLevel','DataSource','Data_Value_Unit',    # Removes 7 columns that are not needed for this analysis
         'Data_Value_Type','Data_Value_Footnote_Symbol',
         'CityFIPS','TractFIPS'], axis =1, inplace=True)

df.shape                                                      # Shows updated count of rows and columns in the dataframe


# In[ ]:


print(df.columns)                                # Provides list of all column names


# In[ ]:


headers = list(df.columns.values)                # Creates headers object that will be updated in the next steps
print(headers)                                   # Shows contents of 'headers'


# In[ ]:


headers[1] = 'ST'                 # Renaming certain column headers
headers[2] = 'State'
headers[3] = 'City'
headers[5] = 'Location_ID'
headers[6] = 'Measure_Desc'
headers[7] = 'DV_Type'
headers[9] = 'Low_CL'
headers[10] = 'High_CL'
headers[11] = 'DV_Footnote'
headers[12] = 'Population'
headers[13] = 'Geo_Loc'
headers[14] = 'Category_ID'
headers[15] = 'Measure_ID'
headers[16] = 'Measure'
df.columns = headers              # Using updated header names for the columns in the dataframe
print(df.columns)                 # Shows updated column names for the dataframe


# In[ ]:


df.head(3)                        # Shows first three rows of the dataframe with the updated column names


# In[ ]:


df['Target'] = np.nan   # Adds new column called "Target" to the dataframe; this will be populated later for classification
df.dtypes               # Indicates data type for each column, including the new column called "Target"


# In[ ]:


df = df[['Year','ST','State','City','Population','Category_ID','Category',    # Reorders the columns in the dataframe
        'Measure_ID','Measure','DV_Type','Data_Value','Low_CL','High_CL',
        'Target','DV_Footnote','Measure_Desc','Location_ID','Geo_Loc']]

df.head(3)    # Shows first 3 rows of the dataframe; confirms that the columns have been reordered


# In[ ]:


df.shape      # Shows count of rows and columns in the dataframe

