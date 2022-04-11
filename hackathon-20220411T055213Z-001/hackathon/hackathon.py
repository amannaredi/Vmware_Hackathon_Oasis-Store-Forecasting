from random import random

from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)




@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    pred= "Value displayed here"
    return render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
