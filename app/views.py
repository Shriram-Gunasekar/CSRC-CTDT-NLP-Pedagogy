from . import db
from .models import Account

from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__, url_defaults=None, root_path=None ) #template_folder not specified

@views.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        text = request.form.get('option')
        answer = "Your text has been summarized"
        return render_template('dashboard.html', user=current_user, answer=answer)
    return render_template('dashboard.html', user=current_user)

@views.route('/plagsim', methods=['GET','POST'])
@login_required
def plagsim():
    if request.method == 'POST':
        ortext = request.form.get('theirplagdata')
        duptext = request.form.get('checkplagdata')
        orfile = request.files['theirplagfile']
        dupfile = request.files['checkplagfile']
        print(orfile.read())
        similarity = 'this is old'
        if orfile and dupfile:
            similarity = 'this is new'
        return render_template('plagsim.html', user=current_user, similarity=similarity)
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






























































































      





