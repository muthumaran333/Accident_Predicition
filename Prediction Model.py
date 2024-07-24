import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Load the data
df = pd.read_csv('accidents_india.csv')

# Data Cleaning

# Drop rows with any NaN values
df.dropna(inplace=True)

# Fill NaN values in specific columns with the mean
df['Sex_Of_Driver'] = df['Sex_Of_Driver'].fillna(df['Sex_Of_Driver'].mean())
df['Vehicle_Type'] = df['Vehicle_Type'].fillna(df['Vehicle_Type'].mean())
df['Speed_limit'] = df['Speed_limit'].fillna(df['Speed_limit'].mean())
df['Road_Type'] = df['Road_Type'].fillna(df['Road_Type'].mean())
df['Number_of_Pasengers'] = df['Number_of_Pasengers'].fillna(df['Speed_limit'].mean())

# Convert categorical values into numerical values

# Encode categorical variables
label_encoders = {}
categorical_columns = df.select_dtypes(include=['object']).columns

print("Before Encoding:")
for column in categorical_columns:
    print(f"{column}: {df[column].unique()}")


for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])


print("\nAfter Encoding:")
for column in categorical_columns:
    print(f"{column}: {df[column].unique()}")


# Encode more categorical variables
c = LabelEncoder()
df['Day'] = c.fit_transform(df['Day_of_Week'])
df.drop('Day_of_Week', axis=1, inplace=True)
l = LabelEncoder()
df['Light'] = l.fit_transform(df['Light_Conditions'])
df.drop('Light_Conditions', axis=1, inplace=True)
s = LabelEncoder()
df['Severity'] = s.fit_transform(df['Accident_Severity'])
df.drop('Accident_Severity', axis=1, inplace=True)

# Prepare data for training
x = df.drop(['Pedestrian_Crossing', 'Special_Conditions_at_Site', 'Severity'], axis=1)
y = df['Severity']

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.86)

# Train and evaluate Logistic Regression model
tru = LogisticRegression()
tru.fit(x_train, y_train)
print(f"Logistic Regression Accuracy: {tru.score(x_test, y_test)}")

# Confusion matrix
yp = tru.predict(x_test)
cm = confusion_matrix(y_test, yp)
print(f"Confusion Matrix:\n{cm}")

# Model Saving and Loading
input_data = [int(x) for x in "2 10 201 10 10 8 3".strip().split()]
input_df = pd.DataFrame([input_data], columns=x_train.columns)
b = tru.predict(input_df)
pickle.dump(tru, open('test1.pkl', 'wb'))
test = pickle.load(open('test1.pkl', 'rb'))

print(f"Prediction: {b}")
