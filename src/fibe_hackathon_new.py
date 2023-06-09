# -*- coding: utf-8 -*-
"""Fibe_Hackathon_new.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FnzDasdhUvLeHQW0SNTfMqYrVK0UEtdn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/lending_club_loan_two.csv")

df.info()

#EXPLORATORY DATA ANALYSIS

sns.countplot(x="loan_status", data=df)

plt.figure(figsize=(12,4))
sns.histplot(x="loan_amnt", data=df, bins=40)

df.corr()

plt.figure(figsize=(12,7))
sns.heatmap(df.corr(), annot=True, cmap="viridis")

sns.scatterplot(x="installment", y="loan_amnt", data=df)

sns.boxplot(x="loan_status", y="loan_amnt", data=df)

df.groupby("loan_status")["loan_amnt"].describe()

df["grade"].unique()

df["sub_grade"].unique()

sns.countplot(x="grade", data=df, hue="loan_status")

plt.figure(figsize=(12,4))
subgrade_order = sorted(df["sub_grade"].unique())
sns.countplot(x="sub_grade", data=df, palette="coolwarm", order=subgrade_order)

plt.figure(figsize=(12,4))
subgrade_order = sorted(df["sub_grade"].unique())
sns.countplot(x="sub_grade", data=df, palette="coolwarm", order=subgrade_order, hue="loan_status")

df["loan_repaid"] = df["loan_status"].map({"Fully Paid":1, "Charged Off":0})

df[["loan_repaid","loan_status"]]

df.corr()["loan_repaid"].sort_values().drop("loan_repaid").plot(kind="bar")

#DATA PREPROCESSING

df.head()

len(df)

df.isnull().sum()

100* df.isnull().sum()/len(df)

df["emp_title"].nunique()

df["emp_title"].value_counts()

df = df.drop("emp_title", axis=1)

sorted(df["emp_length"].dropna().unique())

emp_length_order = [ '< 1 year',
 '1 year',
 '2 years',
 '3 years',
 '4 years',
 '5 years',
 '6 years',
 '7 years',
 '8 years',
 '9 years',
 '10+ years']

plt.figure(figsize=(12,4))
sns.countplot(x="emp_length",data=df,order=emp_length_order)

plt.figure(figsize=(12,4))
sns.countplot(x="emp_length",data=df,order=emp_length_order, hue="loan_status")

emp_co = df[df["loan_status"]=="Charged Off"].groupby("emp_length").count()["loan_status"]

emp_fp = df[df["loan_status"]=="Fully Paid"].groupby("emp_length").count()["loan_status"]

#Direct ratio
#emp_co/emp_fp

#Percentage will be
emp_co/(emp_co+emp_fp)

emp_len = emp_co/(emp_co+emp_fp)

emp_len.plot(kind="bar")

df = df.drop("emp_length", axis=1)

df.isnull().sum()

df["purpose"].head(10)

df['title'].head(10)

df = df.drop("title", axis=1)

df["mort_acc"].value_counts()

df.corr()["mort_acc"].sort_values()

df.groupby("total_acc").mean()["mort_acc"]

total_acc_avg = df.groupby("total_acc").mean()["mort_acc"]
#The average "mort_acc" for the different groups of "total_acc"
#So "total_acc_avg" is our Lookup

def fill_mort_acc(total_acc,mort_acc):
    if np.isnan(mort_acc): #if we are missing the "mort_acc" value
        return total_acc_avg[total_acc] #lookup the average value for the mort_acc based off the total_acc
    else:
        return mort_acc #if it's not missing, just return the mort_acc value

df["mort_acc"] = df.apply(lambda x: fill_mort_acc(x["total_acc"],x["mort_acc"]),axis=1) #a function to two columns of Pandas dataframe

df.isnull().sum()["mort_acc"] #confirming if we still have null values in "mort_acc"

df.isnull().sum()

df = df.dropna() #removing rows that contain missing values

df.isnull().sum() #checking the success of the last task

df.info()

df.select_dtypes(["object"]).columns

df['sub_grade'].unique()

sub_grade_mapping = {
    'A1': 1,
    'A2': 2,
    'A3': 3,
    'A4': 4,
    'A5': 5,
    'B1': 6,
    'B2': 7,
    'B3': 8,
    'B4': 9,
    'B5': 10,
    'C1': 11,
    'C2': 12,
    'C3': 13,
    'C4': 14,
    'C5': 15,
    'D1': 16,
    'D2': 17,
    'D3': 18,
    'D4': 19,
    'D5': 20,
    'E1': 21,
    'E2': 22,
    'E3': 23,
    'E4': 24,
    'E5': 25,
    'F1': 26,
    'F2': 27,
    'F3': 28,
    'F4': 29,
    'F5': 30,
    'G1': 31,
    'G2': 32,
    'G3': 33,
    'G4': 34,
    'G5': 35
}

df['sub_grade'] = df['sub_grade'].map(sub_grade_mapping)

#term
df["term"].value_counts()

df["term"] = df["term"].apply(lambda term: int(term[:3]))

df["term"]

df["term"].value_counts()

#grade feature

df = df.drop("grade", axis=1)

df.columns

df.verification_status.unique()

verification_mapping = {
    'Not Verified': 0,
    'Source Verified': 1,
    'Verified': 2
}

df['verification_status'] = df['verification_status'].map(verification_mapping)

df.application_type.unique()

application_type_mapping = {
    'INDIVIDUAL': 0,
    'JOINT': 1,
    'DIRECT_PAY': 2
}

df['application_type'] = df['application_type'].map(application_type_mapping)

df.initial_list_status.unique()

initial_list_status_mapping = {
    'w': 0,
    'f': 1
}

df['initial_list_status'] = df['initial_list_status'].map(initial_list_status_mapping)

df.purpose.unique()

purpose_mapping = {
    'vacation': 0,
    'debt_consolidation': 1,
    'credit_card': 2,
    'home_improvement': 3,
    'small_business': 4,
    'major_purchase': 5,
    'other': 6,
    'medical': 7,
    'wedding': 8,
    'car': 9,
    'moving': 10,
    'house': 11,
    'educational': 12,
    'renewable_energy': 13
}

df['purpose'] = df['purpose'].map(purpose_mapping)

df.select_dtypes(["object"]).columns

df.columns

#home_ownership
df["home_ownership"].value_counts()

df["home_ownership"] = df["home_ownership"].replace(["NONE","ANY"],"OTHER")

df["home_ownership"].value_counts()

df.home_ownership.unique()

home_ownership_mapping={
    'RENT': 0,
    'MORTGAGE': 1,
    'OWN':2,
    'OTHER':3
}

df['home_ownership'] = df['home_ownership'].map(home_ownership_mapping)

df = df.drop("address", axis=1)

df = df.drop("issue_d", axis=1)

df["earliest_cr_line"]

df["earliest_cr_line"] = df["earliest_cr_line"].apply(lambda date: int(date[-4:]))

df["earliest_cr_line"]

df.info()

from sklearn.model_selection import train_test_split

df = df.drop("loan_status", axis=1)

X = df.drop("loan_repaid", axis=1).values
y = df["loan_repaid"].values

print(len(df))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100)

rfc.fit(X_train,y_train)

rfc_y_pred = rfc.predict(X_test)

accuracy_score(y_test,rfc_y_pred)

# saving the model 
import pickle 
pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(rfc, pickle_out) 
pickle_out.close()