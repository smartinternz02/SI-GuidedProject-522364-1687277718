from flask import Flask,render_template,request

import pickle
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
app=Flask(__name__,template_folder='templates')
model=pickle.load(open('model1.pkl','rb'))
@app.route('/')
def home():
    return render_template('use.html')
@app.route('/Prediction/',methods=["POST","GET"])
def prediction():
    return render_template('use1.html')
@app.route('/Home/',methods=["POST","GET"])
def my_home():
    return render_template('use.html')
@app.route('/predict/',methods=["POST","GET"])
def predict():
    input_feature=[float(x) for x in request.form.values() ]  
    features_values=[np.array(input_feature)]
    feature_name=['cab_type', 'name','product_id','source','destination']
    x=pd.DataFrame(features_values,columns=feature_name)
    prediction=model.predict(x)  
    print("Prediction is:",prediction)
    return render_template("finalresult.html",prediction=prediction[0])
if __name__=="__main__":
    
    
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)