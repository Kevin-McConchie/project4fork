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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/form.html", methods=['POST',' GET' ])
def form():
    if request.methods == 'POST':
        # print(request.form)
        
        # create df with input values for testing
        array =[x for x in request.form.values()]
        print(array)
        input_df = pd.DataFrame({'entry1':[array[0]],
        'entry2':[array[1]],
        'entry3':[array[2]],
        'entry4':[array[3]],
        'entry5':[array[4]],
        'entry6':[array[5]],
        'entry7':[array[6]],
        'entry8':[array[7]],
        'entry9':[array[8]],
        'entry10':[array[9]],
        'entry11':[array[10]]})
        
        # Apply scaler to input data
        X_scaler= joblib.load('X_scaler.sav')
        # predict outcome
        model = joblib.load('LogisticRegression.sav')
        scaled_result = X_scaler.transform(np.array(input_df))
        predict = model.predict(scaled_result)
        
        if predict[0]==1:
            result = "Customer will Stay"
        else:
            result = "Customer will churn"    
        input_df['Outcome']=result
        # input_df.to_csv("Outcome.csv")    
        print (result)
    return render_template("index.html",result=result)



if __name__ == "__main__":
    app.run(debug=False)

# 


