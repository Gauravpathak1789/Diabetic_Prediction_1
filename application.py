from flask import Flask, render_template, request, app, Response
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app=application
scaler=pickle.load(open("Model/scaler_diabetic.pkl","rb"))
model=pickle.load(open("Model/diabt_log.pkl","rb"))


@app.route('/',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'Diabetic'
        else:
            result ='Non-Diabetic'
            
        return render_template('home.html',result=result[0:])

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")