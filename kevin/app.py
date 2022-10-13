### Dependencies and set up
from flask import Flask, render_template, jsonify, request, redirect
import joblib
import numpy as np
import sklearn

app = Flask(__name__)



### Routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def returnhome():
    return render_template("index.html")



@app.route("/predictions.html", methods=['POST',' GET' ])
def predictions():
    if request.methods == 'POST':
        # print(request.form)
        array =[x for x in request.form.values()]
        print(input)
        X= request.form.values()
        # X= np.ravel(X)
        X_scaler= joblib.load('Xscaler.sav')
        model = joblib.load('LogisticRegression.sav')
        scaled_results = X_scaler.transform(np.array(input))
        result = model.predict(scaled_results)
        
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=False)

# 