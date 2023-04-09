
# CreditAssure
This is the project submitted by **Team_RN** for the Fibe-hack the vibe hackathon. Our project aims to develop an application that can accurately predict whether a person will default on their loan or make timely payments.

## Problem Statement

Credit scoring is a statistical analysis performed by lenders and financial institutions to determine the ability of a person or a small, owner-operated business to repay. Lenders use credit scoring to help decide whether to extend or deny credit as for any organization, even the slightest chance of financial risk can not be ignored or ruled out. The objective of this challenge is to create a robust machine-learning model to predict which individuals are most likely to default on their loans, based on their historical loan repayment behavior and transactional activities

## Dataset
This dataset contains information on loans made through the **Lending Club platform**, a peer-to-peer lending company that connects borrowers with investors. The dataset includes data on loans issued between *2007* and *2018*.

The goal of this dataset is to predict whether a borrower will **fully pay** off their loan or **default**.

### Dataset Columns
The dataset includes the following 27 columns:
* **loan_amnt:** The listed amount of the loan applied for by the borrower.
* **term:** The number of payments on the loan. Values are in months and can be either 36 or 60.
* **int_rate:** Interest Rate on the loan.
* **installment:** The monthly payment owed by the borrower if the loan originates.
* **grade:** LC assigned loan grade.
* **sub_grade:** LC assigned loan subgrade.
* **emp_title:** The job title supplied by the borrower when applying for the loan
* **emp_length:** Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years.
* **home_ownership:** The home ownership status provided by the borrower during registration or obtained from the credit report.
* **annual_inc:** The self-reported annual income provided by the borrower during registration.
* **verification_status:** Indicates if income was verified by LC, not verified, or if the income source was verified.
* **issue_d:** The month which the loan was funded.
* **loan_status:** Current status of the loan.
* **purpose:** A category provided by the borrower for the loan request.
* **title:** The loan title provided by the borrower.
* **zip_code:** The first 3 numbers of the zip code provided by the borrower in the loan application.
* **addr_state:** The state provided by the borrower in the loan application.
* **dti:** A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.
* **earliest_cr_line:** The month the borrower's earliest reported credit line was opened.
* **open_acc:** The number of open credit lines in the borrower's credit file.
* **pub_rec:** Number of derogatory public records.
* **revol_bal:** Total credit revolving balance.
* **revol_util:** Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
* **total_acc:** The total number of credit lines currently in the borrower's credit file.
* **initial_list_status:** The initial listing status of the loan. Possible values are – W, F.
* **application_type:** Indicates whether the loan is an individual application or a joint application with two co-borrowers.
* **mort_acc:** Number of mortgage accounts.
* **pub_rec_bankruptcies:** Number of public record bankruptcies.

### Target Variable
The target variable for this dataset is the **loan_status** column. This column indicates whether the borrower has fully paid off their loan or has defaulted.

A value of "Fully Paid" indicates that the borrower has fully paid off their loan, while a value of "Default" indicates that the borrower has failed to pay off the loan

### Source
This dataset was obtained from Kaggle. It was originally compiled by Lending Club and made available through Kaggle.

## Project Overview :
1. **Exploratory Data Analysis:** This step involves analyzing and understanding the data. It includes data visualization, identifying missing values, outliers, and understanding the relationship between the features.
2. **Data Cleaning:** In this step, we handle missing values, outliers, and remove irrelevant features that are not useful in our analysis.
3. **Categorical to Numerical:** We convert categorical variables into numerical ones using different encoding techniques.
4. **Feature Engineering:** We create new features from existing ones that may improve our model's performance.
5. **Model Training:** Model training using various algorithms such as Logistic Regression, XGBoost, Artificial Neural Networks (ANN), and Random Forest Classifier (RFC).
6. **Front-end Development:** We create a user-friendly front-end using Streamlit, a Python library for building interactive web applications.

## Model Training :
We trained our model using various Machine Learning algorithms such as **Logistic Regression, XGBoost, Artificial Neural Networks (ANN), and Random Forest Classifier (RFC)**. The following table shows the accuracy achieved by each model:

| Models                  | Accuracy               |
| ----------------------- | ---------------------- |
| ANN                     | 0.8036283588887202     |
| XGBoost                 | 0.8050199888669601     |
| Logistic Regression     | 0.8034891958908962     |
| Random Forest Classifier| 0.8034891958908962     |

Based on the accuracy achieved, we selected the Random Forest Classifier as our final model.

## Deployment :
We deployed the Random Forest Classifier model using a Streamlit front-end, allowing users to input loan information and receive a prediction of whether the loan will be fully paid or will default.

### Project Preview :
![c](https://user-images.githubusercontent.com/79302868/230738791-ae477569-a4ef-4077-8d82-a89628307fe7.jpg)

## Repository Structure:
- data: 
  - Contains the dataset used for the project. 
  - Link for the dataset: https://drive.google.com/file/d/1cd2f_wbIY1NyMSX6gL-eZUSir25Ipj-x/view?usp=sharing
- src: 
  - Contains necessary files required for the development of a user interface that utilizes the streamlit platform.
    - app.py: Contains the Streamlit front-end code for the deployed application.
    - classifier.pkl: Contains saved trained model
    - Fibe_Hackathon_streamlit.py: Contains code for integrating and connecting the "app.py" file with a model.
    - SessionState.py: Contains code to help you create session for your app.  
- models: 
  - Contains the trained model.
    - ANN.ipynb
    - XGBoost.ipynb
    - RFC.ipynb
    - LR.ipynb

## Installation :
### Requirements :
* Python 3.6 or higher
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Keras
* Tensorflow
* Streamlit

### Installation :
To install the project, first clone the repository:

```
git clone 'https://github.com/rishika10bhalla/FibeHackathon_TeamRN'
```

Then, install the required packages from requirements.txt

### Running the project :
To run the deployed application, navigate to the project directory in your command prompt or terminal and run the following command:

```
streamlit run app.py
```

This will launch the application in your browser, where you can input loan information and receive a prediction of whether the loan will be fully paid or will default.

The `app.py` file in the `src` directory contains the Streamlit front-end code for the deployed application.

## Conributors :
- [Rishika Bhalla](https://github.com/rishika10bhalla)
- [Nishtha Jain](https://github.com/2002nishthajain)

