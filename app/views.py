from . import db
from .models import Account
from .eval import result
from . import qamodel
from . import summarymodel
from . import semsimmodel

from . import geometrymodel
from . import grademodel
from . import profilemodel
from . import geometryvectorizer
from . import gradevectorizer
from . import profilevectorizer

from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for

from sentence_transformers import util

import json
responses = json.load(open('answers.json'))
responses = responses['answers']
import os

from sklearn.feature_extraction.text import CountVectorizer

from PyPDF2 import PdfReader

vectorizer = CountVectorizer(binary=True)

views = Blueprint('views', __name__, url_defaults=None, root_path=None ) #template_folder not specified

# Dashboard
@views.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        message = request.form.get('message')
        scores = []
        for i in responses:
            scores.append(plagresult(message,i))
        answer = responses[scores.index(max(scores))]
        code = scores.index(max(scores))
        print(type(code))
        return render_template('dashboard.html', user=current_user, response=answer, code=code)
    return render_template('dashboard.html', user=current_user,response='', code='')

# General Services
@views.route('/evaluator', methods=['GET', 'POST'])
@login_required
def evaluator():
    if request.method == 'POST':
        theirpdf = request.files['answer']
        checkpdf = request.files['key']
        if theirpdf and checkpdf:
            theirpdf.save(theirpdf.filename)
            checkpdf.save(checkpdf.filename)
            theirpdfdata = PdfReader(theirpdf.filename)
            checkpdfdata = PdfReader(checkpdf.filename)
            theirpdfdata = ''.join([theirpdfdata.pages[i].extract_text() for i in range(len(theirpdfdata.pages))])
            checkpdfdata = ''.join([checkpdfdata.pages[i].extract_text() for i in range(len(checkpdfdata.pages))])
            os.remove(theirpdf.filename)
            os.remove(checkpdf.filename)
            semscore = plagresult(theirpdfdata,checkpdfdata)
            scores = result(theirpdfdata,checkpdfdata)
            jaccscore = scores[0]
            cosinescore = scores[1]
            eucscore = scores[2]
            manscore = scores[3]
            return render_template('evaluator.html', user=current_user, semscore=semscore, jaccscore=jaccscore, cosinescore=cosinescore, eucscore=eucscore, manscore=manscore)
    return render_template('evaluator.html', user=current_user, simscore="")


@views.route('/plagsim', methods=['GET','POST'])
@login_required
def plagsim():
    if request.method == 'POST':
        theirplagtext = request.form.get('theirplagtext')
        checkplagtext = request.form.get('checkplagtext')
        if theirplagtext and checkplagtext:
            simscore = plagresult(theirplagtext,checkplagtext)
            simscore = round(simscore.item()*100, 2)
        else:
            simscore = "Enter Valid Inputs"
        return render_template('plagsim.html', user=current_user, simscore=simscore)
    return render_template('plagsim.html', user=current_user, simscore="")

@views.route('/pdfsim', methods=['GET','POST'])
@login_required
def pdfsim():
    if request.method == 'POST':
        theirpdf = request.files['theirpdf']
        checkpdf = request.files['checkpdf']
        if theirpdf and checkpdf:
            theirpdf.save(theirpdf.filename)
            checkpdf.save(checkpdf.filename)
            theirpdfdata = PdfReader(theirpdf.filename)
            checkpdfdata = PdfReader(checkpdf.filename)
            theirpdfdata = ''.join([theirpdfdata.pages[i].extract_text() for i in range(len(theirpdfdata.pages))])
            checkpdfdata = ''.join([checkpdfdata.pages[i].extract_text() for i in range(len(checkpdfdata.pages))])
            os.remove(theirpdf.filename)
            os.remove(checkpdf.filename)
            simscore = plagresult(theirpdfdata,checkpdfdata)        
        return render_template('pdfsim.html', user=current_user, simscore=simscore)
    return render_template('pdfsim.html', user=current_user, simscore="")

@views.route('/bertsum', methods=['GET','POST'])
@login_required
def bertsum():
    if request.method == 'POST':
        theirsumtext = request.form.get('theirsumtext')
        textsentences = request.form.get('textsentences')
        if theirsumtext:
            textsummary = summarizer(theirsumtext,sentences=textsentences)
        else:
            textsummary = "Please Enter Valid Input"
        return render_template('bertsum.html', user=current_user,textsummary=textsummary)
    return render_template('bertsum.html',user=current_user,textsummary="")

@views.route('/pdfsum', methods=['GET','POST'])
@login_required
def pdfsum():
    if request.method == 'POST':
        theirpdf = request.files['theirpdf']
        textsentences = request.form.get('textsentences')
        if theirpdf:
            theirpdf.save(theirpdf.filename)
            theirpdfdata = PdfReader(theirpdf.filename)
            theirpdfdata = ''.join([theirpdfdata.pages[i].extract_text() for i in range(len(theirpdfdata.pages))])
            os.remove(theirpdf.filename)
            textsummary = summarizer(theirpdfdata,sentences=textsentences)
        return render_template('pdfsum.html', user=current_user,textsummary=textsummary)
    return render_template('pdfsum.html',user=current_user,textsummary="")

@views.route('/qa', methods=['GET','POST'])
@login_required
def qa():
    if request.method == 'POST':
        theirqatext = request.form.get('theirqatext')
        theirqas = request.form.get('theirqas')
        if theirqatext and theirqas:
            answers = qaanswers(theirqatext, theirqas.split(';'))
            #answers = "".join(i for i in answers)
        else:
            answers = "Inputs are not valid. Please Enter Q's separates by semicolons for your text data"
        return render_template('qa.html',user=current_user, answers=answers)
    return render_template('qa.html',user=current_user,answers="")

@views.route('/pdfqa', methods=['GET','POST'])
@login_required
def pdfqa():
    if request.method == 'POST':
        theirpdf = request.files['theirpdf']
        theirqas = request.form.get('theirqas')
        if theirpdf and theirqas:
            theirpdf.save(theirpdf.filename)
            theirpdfdata = PdfReader(theirpdf.filename)
            theirpdfdata = ''.join([theirpdfdata.pages[i].extract_text() for i in range(len(theirpdfdata.pages))])
            os.remove(theirpdf.filename)
            answers = qaanswers(theirpdfdata, theirqas.split(';'))
        return render_template('pdfqa.html',user=current_user, answers=answers)
    return render_template('pdfqa.html',user=current_user,answers="")

# Department Services

@views.route('/machining',methods=['GET','POST']) 
@login_required
def machining():
    if request.method == 'POST':
        option = request.form.get('option')
        query = request.form.get('query')
        answer = recommender(query,option)
        return render_template('machining.html',user=current_user, answer=answer, option=option )
    return render_template('machining.html',user=current_user, answer='', option='')

@views.route('/qaentomology', methods=['GET', 'POST'])
@login_required
def qaentomology():
    if request.method == 'POST':
        concept = request.form.get('concept')
        question = request.form.get('query')
        data = json.load(open('entomology.json'))
        concept = data[concept]
        answer = qaanswers(concept, question.split(';'))
        return render_template('qaentomology.html',user=current_user, answer=answer)
    return render_template('qaentomology.html', user=current_user, answer='')

#Model Methods     

def qaanswers(theirqatext, theirqas):
    answers = []
    temp = ''
    for i in theirqas:
        temp = qamodel({'context':theirqatext,'question': i})
        answers.append((i,temp['answer'],round(temp['score']*100,2)))
    return answers

def plagresult(text1,text2):
    text1_representation = semsimmodel.encode(text1)
    text2_representation = semsimmodel.encode(text2)
    cosine_sim = util.pytorch_cos_sim(text1_representation,text2_representation)   
    return cosine_sim 

def summarizer(data,sentences=5):
    answer = summarymodel(data, num_sentences=int(sentences), min_length=5)
    return answer

def recommender(text, option):
    if option == 'insertgrade':
        text = gradevectorizer.transform([text])
        return grademodel.predict(text)
    if option == 'insertgeometry':
        text = geometryvectorizer.transform([text])
        return geometrymodel.predict(text)
    if option == 'insertprofile':
        text = profilevectorizer.transform([text])
        return profilemodel.predict(text)

def evaluator(text):
    pass