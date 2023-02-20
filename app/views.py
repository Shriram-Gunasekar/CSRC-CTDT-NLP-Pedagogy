from . import db
from .models import Account
from . import qamodel
from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__, url_defaults=None, root_path=None ) #template_folder not specified

@views.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    qamodel1 = qamodel
    if request.method == 'POST':
        text = request.form.get('option')
        answer = "Your text has been summarized"
        return render_template('dashboard.html', user=current_user, answer=answer)
    return render_template('dashboard.html', user=current_user)

@views.route('/plagsim', methods=['GET','POST'])
@login_required
def plagsim():
    if request.method == 'POST':
        orfile = request.form.get('theirplagfile')
        dupfile = request.form.get('checkplagfile')
        ortext = request.form.get('theirplagtext')
        duptext = request.form.get('checkplagtext')
        if orfile and dupfile:
            orfile = orfile.read()
            dupfile = dupfile.read()
            filescore = plagresult(orfile, dupfile)
        elif ortext and duptext:
            textscore = plagresult(ortext, duptext)
        else:
            score = "Please upload your text file or paste your text in the text box"
        return render_template('plagsim.html', user=current_user, score=score)
    return render_template('plagsim.html', user=current_user)

@views.route('/bertsum', methods=['GET','POST'])
@login_required
def bertsum():
    if request.method == 'POST':
        theirsumtext = request.form.get('theirsumtext')
        theirsumfile = request.files['theirsumfile']
        print(theirsumfile.read())
        summary = 'this is the summary'
        return render_template('bertsum.html', user=current_user, summary=summary)
    return render_template('bertsum.html',user=current_user)

@views.route('/qa')
@login_required
def qa():
    return render_template('qa.html',user=current_user)

@views.route('/eval')
@login_required
def eval():
    return render_template('eval.html',user=current_user)


def answer(args):
    return args

def plagresult(plagscore):
    return plagscore

def summarizer(summary):
    return summary


























































































      





