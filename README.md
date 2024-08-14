## Predicting Subscription to Term Deposits

### Project Overview
This project involves predicting whether a client will subscribe to a term deposit based on a dataset related to direct marketing campaigns of a Portuguese banking institution. The primary objective is to build a model that accurately predicts the subscription status (yes/no) based on various client attributes and campaign details.

### Dataset
The dataset used in this analysis contains the following columns:
- **Age**: Age of the client.
- **Job**: Job type of the client.
- **Marital**: Marital status of the client.
- **Education**: Education level of the client.
- **Credit_default**: Has credit in default? (binary: "yes","no")
- **Housing_loan**: Has housing loan? (binary: "yes","no")
- **Personal_loan**: Has personal loan? (binary: "yes","no")
- **Contact_type**: Contact communication type.
- **Last_contact_month**: Last contact month of year.
- **Last_contact_day**: Last contact day of the week.
- **Duration**: Last contact duration, in seconds.
- **Cur_campaign_counts**: Number of contacts performed during this campaign and for this client.
- **Days_since_last_contact**: Number of days that passed by after the client was last contacted from a previous campaign.
- **Prev_campaign_counts**: Number of contacts performed before this campaign and for this client.
- **Prev_outcome**: Outcome of the previous marketing campaign.
- **Employment_Var**: Employment variation rate - quarterly indicator.
- **Consumer_price_index**: Consumer price index - monthly indicator.
- **Consumer_confidence_index**: Consumer confidence index - monthly indicator.
- **Euribor_3M**: Euribor 3 month rate - daily indicator.
- **Num_of_employees**: Number of employees - quarterly indicator.
- **Subscription**: Has the client subscribed a term deposit? (binary: "yes", "no")

### Analysis Steps
1. **Data Preparation**:
    - Imported necessary libraries.
    - Loaded the dataset.
    - Checked for null values and duplicates.
    - Removed duplicates.
    - Preprocessed numerical and categorical columns.

2. **Exploratory Data Analysis (EDA)**:
    - **Target Variable Distribution**: Visualized using a count plot.
    - **Distribution of Numerical Features**: Visualized using histograms.
    - **Correlation Matrix of Numerical Features**: Visualized using a heatmap.
    - **Distribution of Categorical Features**: Visualized using count plots.

3. **Data Preprocessing**:
    - Standardized numerical features using `StandardScaler`.
    - One-hot encoded categorical features using `OneHotEncoder`.

4. **Model Building**:
    - Split the dataset into training and testing sets.
    - Defined a pipeline with preprocessing steps and a `DecisionTreeClassifier`.
    - Trained the decision tree classifier on the training set.

5. **Model Evaluation**:
    - Predicted the test set results.
    - Evaluated the classifier using a confusion matrix, classification report, and accuracy score.
    - Performed cross-validation and plotted the cross-validation scores.

### Key Insights
- **Target Variable Distribution**: The dataset is imbalanced with more "no" responses than "yes".
- **Numerical Features**: Distributions of age, duration, and campaign show significant variability.
- **Correlations**: Some features like `emp.var.rate` and `nr.employed` show strong correlations.
- **Categorical Features**: Distribution of job types, marital status, education levels, and contact types provide insights into the client demographics.

### Conclusion
The decision tree classifier provides a baseline model for predicting term deposit subscriptions. Further improvements can be made by exploring other machine learning algorithms, feature engineering, and hyperparameter tuning. The EDA has revealed important patterns and insights that could help in better targeting and improving marketing campaigns.
