import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


def convert_to_value(x):
    if x == 'True':
        return 1
    else:
        return 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Fever= (request.form['fever'])
    print(Fever)
    Tiredness= (request.form['Tiredness'])
    print(Tiredness)
    Dry_Cough= (request.form['Dry-Cough'])
    print(Dry_Cough)
    Difficulty_in_Breathing= (request.form['Difficulty-in-Breathing'])
    print(Difficulty_in_Breathing)
    Sore_Throat= (request.form['Sore-Throat'])
    print(Sore_Throat)
    Pains= (request.form['pain'])
    print(Pains)
    Nasal_Congestion= (request.form['nasal_cong'])
    print(Pains)
    Runny_Nose= (request.form['RN'])
    print(Pains)
    Diarrhea= (request.form['diarrhea'])
    Age_0_9= (request.form['age9'])
    Age_10_19= (request.form['age19'])
    Age_20_24= (request.form['age24'])
    Age_25_59= (request.form['age59'])
    Age_60= (request.form['age60'])    
    Gender= (request.form['gender'])
    Gender_Transgender= (request.form['Gender_Transgender'])
    
    
    
    
    int_features = [convert_to_value(x) for x in request.form.values()]
    print(len(int_features))
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
   
    if prediction[0]==0:
        output = 'You are covid positive.'
    else:
        output = 'You don\'t have covid'

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)