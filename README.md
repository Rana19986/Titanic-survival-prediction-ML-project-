# Titanic-survival-prediction-ML-project-
Built a Machine Learning model to predict Titanic passenger survival using age, gender, class, fare, family size, and embarkation port. Performed data preprocessing, label encoding, EDA, and trained a Logistic Regression model. Achieved 81.01% accuracy and evaluated performance using a confusion matrix and classification report.

#### 1. Project Objective
The goal was to build a machine learning model to determine if a passenger survived based on personal information, including age, gender, ticket class, fare, and family details.

#### 2. Data Overview
The project utilized two datasets (training and testing):
 * **Training Dataset**: Contained 891 entries and 12 columns.
 * **Testing Dataset**: Contained 418 entries and 11 columns.
#### 3. Data Preprocessing
To prepare the data for the model, the following steps were taken:
 * **Missing Values**: Imputed missing 'Age' and 'Fare' values using the median, and 'Embarked' values using the mode.
 * **Feature Selection**: Dropped 'Name', 'Cabin', and 'Ticket' columns as they were deemed unnecessary for the model.
 * **Encoding**: Converted categorical variables ('Sex' and 'Embarked') into numerical formats using LabelEncoder.
#### 4. Model Training & Evaluation
A **Logistic Regression** model was selected for the classification task.
 * **Methodology**: The dataset was split into training and testing sets with a test size of 20%.
 * **Performance**: The model achieved an accuracy of approximately **81.01%** on the test dataset.
**Classification Metrics**:
| Metric | Class 0 (Did Not Survive) | Class 1 (Survived) |
|---|---|---|
| **Precision** | 0.83 | 0.79 |
| **Recall** | 0.86 | 0.74 |
| **F1-Score** | 0.84 | 0.76 |
#### 5. Conclusion
The Logistic Regression model effectively predicted passenger survival with 81.01% accuracy. While the current results are strong, further enhancements could be made by incorporating more advanced machine learning algorithms or refined feature engineering techniques.
