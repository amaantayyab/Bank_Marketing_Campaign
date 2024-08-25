#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis of the Dataset

# # Data Description
# 
# The dataset is related with direct marketing campaigns of a Portuguese banking institution.
# This dataset gives information about the marketing campaigns of the Bank which were based on phone calls. The Task is to analyze the dataset, inorder to find ways to look for future strategies to improve the marketing campaigns for the Bank

# # What is a Term Deposit ?
# 
# A Term Deposit is a bank investment where you deposit a sum of money for a fixed period at a predetermined interest rate. The Funds are
# locked in until the term ends, offering higher interest than a savings account. Its a low risk option with a guaranteed return

# # Importing the Libraries

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Importing the Dataset

# In[70]:


df = pd.read_csv(r"C:\Users\amaan\Desktop\Datasets\bank_data.csv")
df = df.drop(columns=['Unnamed: 0'])


# In[71]:


df.head()


# In[72]:


df.info()


# In[73]:


df.shape


# In[74]:


df.describe()


# In[75]:


# Categorical Features and their unique values
for col in df.select_dtypes(include = 'object').columns:
    print(col)
    print(df[col].unique())


# # Features
# 
# 1) Age | int64 | age in years
# 2) Job | object | type of job (categorical: ['admin.', 'technician', 'services', 'management', 'retired', 'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 'unknown', 'self-employed', 'student'])
# 3) Marital | object | marital status (categorical: ['married', 'single', 'divorced'])
# 4) Education | object | education background (categorical: ['secondary', 'tertiary', 'primary', 'unknown'])
# 5) Credit_default | object | has credit in default? (categorical: ['no', 'yes'])
# 6) Bank_balance | int64 | Balance of the individual
# 7) Housing_loan | object | has housing loan? (categorical: ['yes', 'no'])
# 8) Personal_loan | object | has personal loan? (categorical: ['no', 'yes'])
# 9) Contact_type | object | contact communication type (categorical: ['unknown', 'cellular', 'telephone'])
# 10) Last_contact_day | int64 | last contact day of the week 
# 11) Last_contact_month | object | last contact month of year (categorical: ['may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'jan', 'feb', 'mar', 'apr', 'sep'])
# 12) Call_Duration | int64 | last contact duration, in seconds (numeric)
# 13) Current_campaign_contact | int64 | number of contacts performed during this campaign and for this client
# 14) Days_since_prev_contact | int64 | number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
# 15) Prev_campaign_contact | int64 | number of contacts performed before this campaign and for this client
# 16) Prev_outcome | object | outcome of the previous marketing campaign (categorical: ['unknown', 'other', 'failure', 'success'])
# 
# # Label
# 1) Term_deposit | object | has the client subscribed a term deposit? (binary: 'yes', 'no')
# 

# # Exploratory Data Analysis
# 
# 1) Find Unwanted Columns
# 2) Find Missing Values
# 3) Find Features with One Value
# 4) Explore the Categorical Features
# 5) Find Categorical Feature Distribution
# 6) Relationship between Categorical Features and Label
# 7) Explore the Numerical Features
# 8) Find Discrete Numerical Features
# 9) Find Continuous Numerical Features
# 10) Distribution of Continuous Numerical Features
# 11) Relation between Continuous Numerical Features and Labels
# 12) Find Outliers in Numerical Features
# 13) Explore the Correlation between Numerical Features
# 14) Find Pair Plot
# 15) Check if the Dataset is Balanced
# 

# # Find Unwanted Columns

# - There are no unwanted columns present in the dataset to be removed

# # Find Missing Values

# In[77]:


# find missing values
features_na = [features for features in df.columns if df[features].isnull().sum() > 0]
for feature in features_na:
    print(feature, np.round(df[feature].isnull().mean(), 4),  ' % missing values')
else:
    print("No missing value found")


# - No missing values are found

# # Find Features with One Value

# In[78]:


for column in df.columns:
    print(column, df[column].nunique())


# - No feature with only one value.

# # Explore the Categorical Features

# In[79]:


Categorical_features = [feature for feature in df.columns if ((df[feature].dtypes=='O')&(feature not in ['Term_deposit']))]
Categorical_features


# In[80]:


for feature in Categorical_features:
    print('The feature is {} and number of categories are {}'.format(feature,len(df[feature].unique())))


# - There are Nine Categorical Features
# - Job and Last_contact_month have highest number of unique values

# # Find Categorical Feature Distribution

# In[81]:


#check count based on categorical features
plt.figure(figsize=(15,80), facecolor='white')
plotnumber =1
for Categorical_feature in Categorical_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.countplot(y=Categorical_feature,data=df)
    plt.xlabel(Categorical_feature)
    plt.title(Categorical_feature)
    plotnumber+=1
plt.show()


# - Clients with job type as Management are very high in given dataset and Housemaid are very less.
# - Clients who are married are high in given dataset compared to the Divorced.
# - Clients with Education background as secondary are in high numbers in given dataset
# - Credit_default feature seems to play no significance because the Ratio of NO is very high and YES is negligible.
# - Data is very high in the Month of May and very less in the Month of Dec

# # Relationship between Categotical Features and Label

# In[82]:


#Check target label split over categorical features
#TO find out the relationship between categorical variable and dependent variable
for Categorical_feature in Categorical_features:
    sns.catplot(x='Term_deposit', col=Categorical_feature, kind='count', data= df)
plt.show()


# In[83]:


#Check target label split over categorical features and find the count
for Categorical_feature in Categorical_features:
    print(df.groupby(['Term_deposit',Categorical_feature]).size())


# - Retired clients have high interest on Term deposit
# - Clients with housing loan seem to be not interested much on the Term deposit
# - If Previous campaign outcome is Successful then, there is high chance of client to show interest on Term deposit
# - In Month of March, September, October and December, clients show high interest to Term deposit
# - In Month of may, records are very high but Client interest ratio is very less

# # Explore the Numerical Features

# In[84]:


# list of numerical variables
numerical_features = [feature for feature in df.columns if ((df[feature].dtypes != 'O') & (feature not in ['deposit']))]
print('Number of numerical variables: ', len(numerical_features))

# visualise the numerical variables
df[numerical_features].head()


# In[85]:


discrete_feature=[feature for feature in numerical_features if len(df[feature].unique())<25]
print("Discrete Variables Count: {}".format(len(discrete_feature)))


# - There are no Discrete Variables in the Given Dataset

# # Find Continous Numerical Features

# In[86]:


continuous_features=[feature for feature in numerical_features if feature not in discrete_feature+['deposit']]
print("Continuous feature Count {}".format(len(continuous_features)))


# # Distribution of Continous Numerical Features

# In[88]:


#plot a univariate distribution of continues observations
plt.figure(figsize=(20,60), facecolor='white')
plotnumber = 1
for continuous_feature in continuous_features:
    ax = plt.subplot(12, 3, plotnumber)
    sns.histplot(df[continuous_feature], kde=True, ax=ax)  # kde=True adds the KDE line
    plt.xlabel(continuous_feature)
    plotnumber += 1
plt.show()


# - Features Age and Last_contact_day seem to be normally distributed
# - All other Features are heavely skewed towards left and seem to have some outliers too

# # Relation between Continous numerical Features and Labels

# In[90]:


#boxplot to show target distribution with respect numerical features
plt.figure(figsize=(20,60), facecolor='white')
plotnumber =1
for feature in continuous_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.boxplot(x="Term_deposit", y= df[feature], data=df)
    plt.xlabel(feature)
    plotnumber+=1
plt.show()


# - Clients who had Longer Call duration seem to show more Interest 
# 

# # Find Outliers in Numerical Features

# In[91]:


#boxplot on numerical features to find outliers
plt.figure(figsize=(20,60), facecolor='white')
plotnumber =1
for numerical_feature in numerical_features:
    ax = plt.subplot(12,3,plotnumber)
    sns.boxplot(df[numerical_feature])
    plt.xlabel(numerical_feature)
    plotnumber+=1
plt.show()


# - Age, Bank balance, Call Duration, Current & Previous campaigns contacts and Days since last contact has Outliers

# # Explore the Correlation between Numerical Features

# In[93]:


# Checking for Correlation
cor_mat = df.corr(numeric_only=True)

# Plotting the heatmap
fig = plt.figure(figsize=(15, 7))
sns.heatmap(cor_mat, annot=True)
plt.show()


# - It seems like None of the features are heavily correlated with other features

# # Check the Data set is Balanced or not based on Target Values

# In[95]:


#total patient count based on cardio_results
sns.countplot(x='Term_deposit',data=df)
plt.show()


# In[97]:


df['Term_deposit'].groupby(df['Term_deposit']).count()


# - The Dataset is almost Balanced
