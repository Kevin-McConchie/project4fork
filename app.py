### Dependencies and set up
from flask import Flask, render_template, jsonify, request, redirect
import joblib
import numpy as np
import pandas as pd


app = Flask(__name__)

### Routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def returnhome():
    return render_template("index.html")

@app.route("/cleaning.html")
def cleaning():
    return render_template("cleaning.html")

@app.route("/dataprocessing.html")
def dataprocessing():
    return render_template("dataprocessing.html")

@app.route("/models.html")
def models():
    return render_template("models.html")

@app.route("/result.html")
def result():
    return render_template("result.html")



@app.route("/form.html", methods=['POST','GET'])
def form():
    if request.method == 'POST':
        print(request.form)
        
        # create df with input values for testing
        array =[x for x in request.form.values()]
        print(array)
        input_df = pd.DataFrame({'offer':[array[0]],
        'Security':[array[1]],
        'tech_support':[array[2]],
        'contract':[array[3]],
        'Referrals':[array[4]],
        'tenure':[array[5]],
        'monthly_rate':[array[6]],
        'dependants':[array[7]],
        'age':[array[8]],
        'billing':[array[9]],
        'unlimited_data':[array[10]],
        'married':[array[11]],
        })
        
        # Apply scaler to input data
        X_scaler= joblib.load('X_scaler.sav')
        # predict outcome
        model = joblib.load('LogisticRegression.sav')
        scaled_result = X_scaler.transform(np.array(input_df))
        predict = model.predict(scaled_result)
        result=""
        if predict[0]==1:
            return render_template("result.html", result= "Customer will stay.")
        else:
            return render_template("result.html", result= "Customer will churn.")
        # input_df['Outcome']=result
        # input_df.to_csv("Outcome.csv")    
        # print (result)
    return render_template("form.html", result= "")

if __name__ == "__main__":
    app.run(debug=False)

# 


