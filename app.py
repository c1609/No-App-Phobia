from contextlib import _RedirectStream
import numpy as np
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle
from flask import flash 


#create flask app
app = Flask(__name__)

#Load the pickel model
model =pickle.load(open("NoAppPhobiaModel.pkl","rb"))

@app.route('/')
def first():
    return render_template('first.html')

@app.route('/index')
def index():
    return render_template('index.html')
       
@app.route('/starter', methods=['POST'])
def PhobiaPred():
     if request.method == 'POST':
        # Retrieve the form data
        name =request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        working = request.form['working']
        app = request.form['app']
        usage = request.form['usage']
        q = request.form['q']
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']
        q9 = request.form['q9']
        
        formData = [app,age,gender,working,q1,q2,q3,usage,q4,q5,q6,q7,q8,q9,q]
        cleanData = [float(i) for i in formData]
        arr = np.array(cleanData).reshape(1,-1)
        result = model.predict(arr)
        print(result[0])
    
        # Return the result page with severity level
        return render_template('starter.html', data=result,name=name)

if __name__ == '__main__':
    app.run()




