#-------------------------------------------------
# To run this code open a bash terminal
# type : $ uvicorn api:app --reload
# copy/paste the link ex:http://127.0.0.1:8000/... 
# in browser
#-------------------------------------------------

import joblib
import uvicorn
import pickle
import pandas as pd
from fastapi import FastAPI
from pathlib import Path

app = FastAPI()

#Chargement du modèle #ModelClassifier.pkl
model = pickle.load(open('LGBMClassifier.pkl', 'rb'))

#Chargement des données 
#PATH = '../P7_data/data/'
#df = pd.read_parquet(PATH+'test_df.parquet')
df = pd.read_parquet('test_df.parquet')

#Fonction debug
@app.get('/')
async def hello():
    return "API score crédit"

# Fonction d'appel pour la prédiction 
@app.get('/prediction/{client_id}')
async def prediction(client_id: int):

    #selection du client dans le dataframe
    ID = int(client_id)
    X = df[df['SK_ID_CURR'] == ID]

    #selection des colonnes utiles
    ignore_features = ['Unnamed: 0','SK_ID_CURR', 'INDEX', 'TARGET']
    relevant_features = [col for col in df.columns if col not in ignore_features]
    X = X[relevant_features]

    #prédiction
    proba = model.predict_proba(X)
    prediction = model.predict(X)

    dict_final = {
        'prediction' : int(prediction),
        'proba' : float(proba[0][0])
        }

    return (dict_final)



