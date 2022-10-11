### Dependencies and set up
from flask import Flask, render_template, jsonify, request, redirect


app = Flask(__name__)

### Routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def returnhome():
    return render_template("index.html")

@app.route("/preprocessing.html")
def map():
    return render_template("preprocessing.html")

@app.route("/analysis.html")
def dashboard():
    return render_template("analysis.html")

@app.route("/modeling.html")
def dashboard():
    return render_template("modeling.html")

@app.route("/prediction.html")
def dashboard():
    return render_template("predictions.html")






if __name__ == "__main__":
    app.run(debug=False)

# 