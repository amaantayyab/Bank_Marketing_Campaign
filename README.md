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
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

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



