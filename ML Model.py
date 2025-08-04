import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

#import the data 
data=pd.read_csv('insurance2.csv')

#to check the data has any null value or not
data.isnull()

#if there is any null value to drop 
data.dropna(inplace=True)

#divide data into feture and target 
X = data.drop('insuranceclaim', axis=1)  # Features
y = data['insuranceclaim']               # Target

#to split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#fit training data into the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

#fit the predicted values into veriable
y_pred = model.predict(X_test)

#to display the accuracy and other features of the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))

#pkl file to use the result of the machine learning model into chatBot
import joblib

joblib.dump(model, "insurance_model.pkl")

def predict_claim(features_dict):
    df = pd.DataFrame([features_dict])
    prediction = model.predict(df)
    if prediction[0] == 1:
      return "Approved" 
    else :
      return "Rejected"
