# 📈 Bank Marketing Campaign Analysis

## Overview

This project analyzes the direct marketing campaigns of a Portuguese banking institution to develop strategies for improving future campaigns. By leveraging exploratory data analysis and machine learning techniques, specifically using the XGBoost classifier, we aim to predict whether a client will subscribe to a term deposit based on various demographic and campaign-related features.

## Table of Contents

- [Overview](#overview)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Modeling](#modeling)
- [Results](#results)
- [Conclusion](#conclusion)

---

## Dataset Description

The dataset provides information on the marketing campaigns conducted by the bank, which were primarily based on phone calls. The goal is to predict whether a client will subscribe to a term deposit after a marketing contact.

### What is a Term Deposit?

A **Term Deposit** is a bank investment where a sum of money is deposited for a fixed period at a predetermined interest rate. Funds are locked in until the term ends, offering higher interest rates compared to regular savings accounts. It's considered a low-risk investment with guaranteed returns.

### Features

| Feature                     | Type    | Description                                                                                                     |
|-----------------------------|---------|-----------------------------------------------------------------------------------------------------------------|
| **Age**                     | int64   | Age of the client in years.                                                                                     |
| **Job**                     | object  | Type of job (e.g., 'admin.', 'technician', 'services', etc.).                                                   |
| **Marital**                 | object  | Marital status ('married', 'single', 'divorced').                                                               |
| **Education**               | object  | Education background ('secondary', 'tertiary', 'primary', 'unknown').                                           |
| **Credit_default**          | object  | Has credit in default? ('no', 'yes').                                                                           |
| **Bank_balance**            | int64   | Balance of the client.                                                                                          |
| **Housing_loan**            | object  | Has housing loan? ('yes', 'no').                                                                                |
| **Personal_loan**           | object  | Has personal loan? ('no', 'yes').                                                                               |
| **Contact_type**            | object  | Contact communication type ('unknown', 'cellular', 'telephone').                                                |
| **Last_contact_day**        | int64   | Last contact day of the week.                                                                                   |
| **Last_contact_month**      | object  | Last contact month of the year (e.g., 'may', 'jun', 'jul', etc.).                                               |
| **Call_Duration**           | int64   | Duration of the last contact in seconds.                                                                        |
| **Current_campaign_contact**| int64   | Number of contacts performed during this campaign for this client.                                              |
| **Days_since_prev_contact** | int64   | Days passed since the client was last contacted in a previous campaign (999 means not previously contacted).     |
| **Prev_campaign_contact**   | int64   | Number of contacts performed before this campaign for this client.                                              |
| **Prev_outcome**            | object  | Outcome of the previous marketing campaign ('unknown', 'other', 'failure', 'success').                          |
| **Term_deposit**            | object  | **Target variable**: Has the client subscribed to a term deposit? ('yes', 'no').                                |

---


---

## Exploratory Data Analysis (EDA)

Comprehensive EDA was performed to understand the data distribution, identify patterns, and detect anomalies. The following steps were undertaken:

1. **Handling Missing Values**: Identified and addressed missing or null values in the dataset.
2. **Univariate Analysis**: Explored individual features to understand their distributions using histograms and box plots.
3. **Bivariate Analysis**: Analyzed relationships between features and the target variable using bar plots, scatter plots, and correlation matrices.
4. **Outlier Detection**: Detected outliers in numerical features using interquartile range (IQR) and visualized them through box plots.
5. **Feature Distribution**: Examined the distribution of categorical and numerical features.
6. **Data Balance Check**: Checked for class imbalance in the target variable and considered techniques for addressing any imbalance detected.

**Key Insights from EDA**:

- Certain job types and education levels showed higher subscription rates to term deposits.
- Features like `Call_Duration` and `Previous_outcome` had strong correlations with the likelihood of subscribing.
- Some features contained outliers that could affect model performance if not addressed.
- The dataset exhibited a moderate class imbalance, with more instances of clients not subscribing to term deposits.

---

## Feature Engineering

To enhance model performance, several feature engineering techniques were applied:

1. **Dropping Irrelevant Features**: Removed features that did not contribute significantly to the prediction task.
2. **Handling Missing Values**: Imputed missing values using appropriate strategies (e.g., mode for categorical variables).
3. **Encoding Categorical Variables**: Applied one-hot encoding to convert categorical variables into numerical format suitable for modeling.
4. **Feature Scaling**: Standardized numerical features using techniques like Min-Max scaling to normalize the data.
5. **Outlier Treatment**: Addressed outliers by capping and flooring based on percentiles or removing them entirely.
6. **Feature Creation**: Created new features by combining existing ones to capture additional information (e.g., interaction terms).

**Result of Feature Engineering**:

- The processed dataset had improved data quality with reduced noise and variability.
- The transformed features were more suitable for feeding into machine learning algorithms, leading to better model performance.

---

## Modeling

Two machine learning algorithms were evaluated to predict whether a client will subscribe to a term deposit:

1. **Random Forest Classifier**
2. **XGBoost Classifier**

### Model Evaluation

- **Cross-Validation**: Performed 5-fold cross-validation to assess model performance and generalizability.
- **Performance Metrics**: Evaluated models using accuracy, precision, recall, F1-score, and ROC-AUC score.
- **Hyperparameter Tuning**: Employed grid search and random search methods to optimize model hyperparameters.

**Model Selection**:

- The **XGBoost Classifier** outperformed the Random Forest Classifier across all performance metrics.
- **XGBoost** demonstrated better handling of class imbalance and provided more precise predictions.

### Training the Final Model

- Trained the optimized XGBoost model on the full training dataset.
- **Feature Importance**: Plotted feature importance scores to interpret and understand the influence of each feature on predictions.
  
  ![Feature Importance](path/to/feature_importance_plot.png)
  
- **Confusion Matrix**: Generated a confusion matrix to visualize true vs. predicted classifications.
  
  ![Confusion Matrix](path/to/confusion_matrix.png)
  
---

## Results

- **Accuracy**: The final XGBoost model achieved an accuracy of **85.66%** on the test dataset.
- **Precision**: High precision indicates a low false positive rate in predictions.
- **Recall**: Satisfactory recall suggests the model effectively identifies clients who will subscribe.
- **ROC-AUC Score**: The model achieved a strong ROC-AUC score, indicating excellent discriminative ability.

**Interpretation**:

The model effectively predicts client subscription to term deposits, providing valuable insights for tailoring marketing strategies. Features like `Call_Duration`, `Previous_outcome`, and `Age` were among the top contributors to the model's predictions.

---

## Conclusion

The project successfully demonstrated the application of data analysis and machine learning techniques to improve bank marketing campaign outcomes. By identifying key factors influencing client decisions, the bank can:

- **Optimize Targeting**: Focus efforts on demographics and profiles more likely to subscribe.
- **Enhance Communication**: Adjust contact strategies (e.g., timing, method) based on insights.
- **Improve Resource Allocation**: Allocate marketing resources more efficiently to maximize return on investment.






