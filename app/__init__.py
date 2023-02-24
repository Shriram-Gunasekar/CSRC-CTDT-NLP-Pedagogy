from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .setup import config, blueprint, login_det, map
import torch
import pickle

qamodel = torch.load('QA')
summarymodel = torch.load('Summarizer')
semsimmodel = torch.load('Similarity')
#grammar = torch.load('Grammar')
geometrymodel = pickle.load(open('geometrymodel','rb'))
grademodel = pickle.load(open('grademodel','rb'))
profilemodel = pickle.load(open('profilemodel','rb'))
geometryvectorizer = pickle.load(open('geometryvectorizer','rb'))
gradevectorizer = pickle.load(open('gradevectorizer','rb'))
profilevectorizer = pickle.load(open('profilevectorizer','rb'))
convoclassifier = pickle.load(open('convoclassifier','rb'))
convovectorizer = pickle.load(open('convovectorizer','rb'))

db = SQLAlchemy()

def constructor():
    app = Flask(__name__, template_folder = 'templates', static_folder='static')
    config(app)    
    blueprint(app)    
    
    if os.path.exists('app/' + 'tracker.db') == False:
        db.create_all(app=app)
        print('DB Created')
    
    login_det(app)    
    
    map(app)
    
    return app
    
    
    
    




