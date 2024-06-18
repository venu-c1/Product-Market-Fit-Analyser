from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import pickle
import pandas as pd
import numpy as np
le = LabelEncoder()

app = Flask(__name__,template_folder='./templates')

with open('project_marketfit/project/api/m2.pickle', 'rb') as file:
    model = pickle.load(file)
with open('project_marketfit/project/api/model1.pickle','rb') as file1:
    model1=pickle.load(file1)



# @app.route('/predict', methods=['POST'])
# def preprocess_form_data(data):
#     # Convert the colour feature to a one-hot encoded vector
#     colour_map = {'Black': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   'Blue': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                   'Gold': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#                   'Green': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#                   'Grey': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                   'Pink': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                   'Red': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#                   'Rose Gold': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                   'Rose Golden': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#                   'Silver': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}
#     colour = data['colour']
#     colour_encoded = colour_map[colour]

#     # Convert the shape feature to a numerical value
#     shape = data['shape']
#     if shape == 'round':
#         shape_encoded = 0
#     else:
#         shape_encoded = 1

#     # Convert the binary features to numerical values
#     bluetooth = int(data['bluetooth'] == 'Yes')
#     spo2 = int(data['spo2'] == 'Yes')
#     heart_rate = int(data['heart_rate'] == 'Yes')
#     alarm = int(data['alarm'] == 'Yes')
#     distance = int(data['distance'] == 'Yes')
#     sleep = int(data['sleep'] == 'Yes')
#     activity = int(data['activity'] == 'Yes')
#     notifications = int(data['notifications'] == 'Yes')
#     gps = int(data['gps'] == 'Yes')

#     # Create a list of the preprocessed features
#     features = [float(data['price']), float(data['size'])] + colour_encoded + [shape_encoded,
#                 bluetooth, spo2, heart_rate, alarm, distance, sleep, activity, notifications, gps]

#     return features

# Define a Flask route to receive and process the form data
@app.route('/predict',methods=['POST'])
def predict():
    # Receive the form data
    productprice: request.json['productprice']
    style: request.json['style']
    color: request.json['color']
    screensize: request.json['screensize']
    bluetooth: request.json['bluetooth']
    SpO2: request.json['__SpO2']
    heartrate: request.json['heartrate']
    alarmclock: request.json['alarmclock']
    disttracker: request.json['disttracker']
    sleepmonitor: request.json['sleepmonitor']
    acttracker: request.json['acttracker']
    notification: request.json['notification']
    gps: request.json['gps']
    bpmonitor: request.json['bpmonitor']
 #   price = request.form.get('price')
  #  size = request.form.get('size')
    
#    colour = request.form.get('colour')
 #   style=request.form.get('style')
  #  shape = request.form.get('shape')
   # bluetooth = request.form.get('bluetooth')
    #spo2 = request.form.get('spo2')
    #heart_rate = request.form.get('heart_rate')
   # alarm= request.form.get('alarm')
   # distance=request.form.get('distance')
   # sleep = request.form.get('sleep')
   # activity = request.form.get('activity')
   # notifications=request.form.get('notifications')
   # gps = request.form.get('gps')
   # bp = request.form.get('bp')
   
   
    if price != '':
        price = float(price)
    else:
        return jsonify({'error': 'Price cannot be empty.'})
    size=float(size)

    # Preprocess the form data
    # colour_map = {'Black': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #               'Blue': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #               'Gold': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #               'Green': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #               'Grey': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #               'Pink': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #               'Red': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #               'Rose Gold': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #               'Rose Golden': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #               'Silver': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}
    
    # colour_encoded = colour_map[colour]
    if colour == 'Black':
        Black = 1
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0
        
    elif colour == 'Blue':
        Black = 0
        Blue = 1
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0
    
    if colour == 'Gold':
        Black = 0
        Blue = 0
        Gold = 1
        Green = 0
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0
    if colour == 'Green':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 1
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0
    if colour == 'Grey':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 1
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0
    if colour == 'Pink':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 1
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0
    if colour == 'Red':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 0
        Red = 1
        Rose_gold = 0
        Rose_golden = 0
        Silver = 0    
    if colour == 'Rose_gold':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 1
        Rose_golden = 0
        Silver = 0
    if colour == 'Rose_golden':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 1
        Silver = 0
    if colour == 'Silver':
        Black = 0
        Blue = 0
        Gold = 0
        Green = 0
        Grey = 0
        Pink = 0
        Red = 0
        Rose_gold = 0
        Rose_golden = 0
        Silver = 1

    # Convert the shape feature to a numerical value
    if style=='modern':
        style_encoded=0
    else:
        style_encoded=1
        
        
        
     
    if shape == 'round':
        round=1
        square=0
    if shape == 'square':
        round=0
        square=1

    # Convert the binary features to numerical values
    bluetooth = int(['bluetooth'] == 'Yes')
    spo2 = int(['spo2'] == 'Yes')
    heart_rate = int(['heart_rate'] == 'Yes')
    alarm = int(['alarm'] == 'Yes')
    distance = int(['distance'] == 'Yes')
    sleep = int(['sleep'] == 'Yes')
    activity = int(['activity'] == 'Yes')
    notifications = int(['notifications'] == 'Yes')
    gps = int(['gps'] == 'Yes')
    bp=int(['bp'] == 'Yes')

    
    # Create a list of the preprocessed features
    
    data=pd.DataFrame([[price,style_encoded,size,bluetooth,spo2,heart_rate,alarm,distance,sleep,activity,notifications,gps,bp,Black,Blue,Gold,Green,Grey,Pink,Red,Rose_gold,Rose_golden,Silver,round,square]],columns=['price','Style','Screen Size','Bluetooth','SpO2','Heart Rate monitor','Alarm clock','Distance tracker','sleep monitor','Activity tracker','Notifications','gps','bp monitor','Black','Blue','Gold','Green','Grey','Pink','Red','Rose Gold','Rose Golden','Silver','Round','Square'])
    
    prediction=model.predict(data)[0:2]
    prediction2=model1.predict(data)
    if prediction2 ==0:
        result=" lower segment"
    elif  prediction2 ==1:
        
        result="middle segment"
    else:
        
        result= "higher segment"
    # Make a prediction using the pre-trained machine learning model
    




        result = {'output': 'processed data'}
        return jsonify(result)
    
    #return render_template('result.html',prediction=prediction,prediction2=result)



if __name__ == '__main__':
    app.run(debug=True)