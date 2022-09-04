from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import json
import csv
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class today(Resource):
    def get(self,Rain, Temp, Hum, Day):
        #budget = request.args.get('budget')
        #print(budget)
        # Let's load the package
        #budget = [int(budget)]
        df = pd.DataFrame([[Rain, Temp, Hum, Day]])
        model = pickle.load(open('model.pk1', 'rb'))
        prediction = model.predict(df)
        #prediction = int(prediction[0])
        return str(prediction)

class prediction(Resource):
    def get(self, range):
        df = [int(range)]
        #df = pd.DataFrame([[Rain, Temp, Hum, Day]])
        model = pickle.load(open('sarima.pk1', 'rb'))
        predict = model.predict(df)
        return str(predict)
1

#data api
class getData(Resource):
    def get(self):
            df = pd.read_excel('data.xlsx')
            df =  df.rename({'Marketing Budget': 'budget', 'Actual Sales': 'sale'}, axis=1)  # rename columns
            #print(df.head())
            #out = {'key':str}
            res = df.to_json(orient='records')
            #print( res)
            return res

#
api.add_resource(getData, '/api')
api.add_resource(today, '/today/<int:Rain>,<int:Temp>,<int:Hum>,<int:Day>')
api.add_resource(prediction, '/prediction/<int:range>')

if __name__ == '__main__':
    app.run(debug=True)