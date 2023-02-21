from . import db
from .models import Account
#from . import qamodel
from . import summarymodel
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__, url_defaults=None, root_path=None ) #template_folder not specified

@views.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@views.route('/plagsim', methods=['GET','POST'])
@login_required
def plagsim():
    pass

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
    return render_template('bertsum.html',user=current_user)

@views.route('/qa')
@login_required
def qa():
    return render_template('qa.html',user=current_user)

@views.route('/eval')
@login_required
def eval():
    return render_template('eval.html',user=current_user)

def answer(type, question, context):
    pass

def plagresult(plagscore):
    return plagscore

def summarizer(data,sentences):
    answer = summarymodel(data, num_sentences=int(sentences), min_length=5)
    return answer