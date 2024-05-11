#!/usr/bin/env python
# coding: utf-8
# Situation: Amazon, being one of the largest e-commerce platforms, generates vast amounts of sales data daily. As a seller, you're inundated with data from various sources such as product listings, customer orders, and advertising campaigns. Without proper analysis, this data remains untapped potential, hindering informed decision-making and growth.

# # Task: My task is to develop a comprehensive sales report data analysis system that can effectively process, analyze, and interpret Amazon sales data. This system should provide actionable insights to optimize sales performance, enhance marketing strategies, and improve overall business efficiency.

# In[109]:


#Importing libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# # Step 1 :- importing dataset 

# In[46]:


data = pd.read_csv("Amazon Sale Report.csv")


# In[47]:


data.shape


# In[48]:


data.info()


# In[43]:


data.head()


# In[44]:


data.tail()


# # Step 2 :-Data cleaning

# In[50]:


#Checking null values
data.isna().sum()


# In[51]:


#Dropping null values column
data.drop(['New','PendingS'],axis=1,inplace=True)


# In[53]:


data.isna().sum()


# In[55]:


data.dropna(inplace=True)


# In[56]:


data.columns


# In[57]:


#Changing the data type of column float to integer
data['ship-postal-code']=data['ship-postal-code'].astype('int')


# In[58]:


#Coverting data column into datetime 
data['Date']=pd.to_datetime(data['Date'])


# In[59]:


data.info()


# In[60]:


#Statics repretention of the data
data.describe()


# In[110]:


data[['Qty','Amount']].describe()


# #  Step2:-EXPLORATORY DATA ANALYSIS

# In[64]:


df.columns


# In[69]:


ax=sns.countplot(x ='Size',data=data)


# In[73]:


ax=sns.countplot(x='Size',data=data)
for bars in ax. containers:
    ax.bar_label(bars)


# So the above countplot is clearly showing this that we have hight count of Medium size customer

# In[75]:


#Grouping data on the basis of size column
data.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[82]:


size=data.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)
sns.barplot(x='Size',y='Qty',data=size)


# In[86]:


sns.countplot(data=data,x='Courier Status',hue='Status')
plt.show()


# In[90]:


data['Size'].hist()


# In[92]:


data['Category']=data['Category'].astype(str)
column_data=data['Category']
plt.figure(figsize=(10,5))
plt.hist(column_data,bins=30,edgecolor='Black')
plt.show()


# By above barplot we can cleary seen that we have most of sale T-shirt

# In[95]:


#checking b2b data by using pie chart
b2b_check=data['B2B'].value_counts()
plt.pie(b2b_check,labels=b2b_check,autopct='%1.1f%%')
plt.show()


# In[96]:


b2b_check=data['B2B'].value_counts()
plt.pie(b2b_check,labels=b2b_check.index,autopct='%1.1f%%')
plt.show()


# Note : From above chart we can see that maximum i.e. 99.3% of buyers are retailers and 0.7% are B2B buyers

# In[100]:


#  Prepare data for pie chart
a1 = data['Fulfilment'].value_counts()

# Step 4: Plot the pie chart
fig, ax = plt.subplots()

ax.pie(a1, labels=a1.index, autopct='%1.1f%%', radius=0.7, wedgeprops=dict(width=0.6))
ax.set(aspect="equal")

plt.show()


# In[102]:


#Scatter plot
x_data=data['Category']
y_data=data['Size']
plt.scatter(x_data,y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('scatter plot')
plt.show()


# In[104]:


plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show


# In[107]:


# top_10_States 
top_10_state = data['ship-state'].value_counts().head(10)
# Plot count of cities by state
plt.figure(figsize=(12, 6))
sns.countplot(data=data[data['ship-state'].isin(top_10_state.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of  State')
plt.xticks(rotation=45)
plt.show()


# # Conclusion
# The data analysis reveals that the business has a significant customer base in Maharashtra state, mainly serves retailers, fulfills orders through Amazon, experiences high demand for T-shirts, and sees M-Size as the preferred choice among buyers.

# In[ ]:




