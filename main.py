from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI(title="Titanic Survival Prediction API")

# Input schema
class Passenger(BaseModel):
    PassengerId: int
    Pclass: int
    Sex: int          # Male = 1, Female = 0
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int     # C = 0, Q = 1, S = 2

@app.get("/")
def home():
    return {
        "message": "Titanic Survival Prediction API is Running!"
    }

@app.post("/predict")
def predict(data: Passenger):

    df = pd.DataFrame([{
        "PassengerId": data.PassengerId,
        "Pclass": data.Pclass,
        "Sex": data.Sex,
        "Age": data.Age,
        "SibSp": data.SibSp,
        "Parch": data.Parch,
        "Fare": data.Fare,
        "Embarked": data.Embarked
    }])

    prediction = model.predict(df)[0]

    result = "Survived" if prediction == 1 else "Did Not Survive"

    return {
        "prediction": int(prediction),
        "result": result
    }
