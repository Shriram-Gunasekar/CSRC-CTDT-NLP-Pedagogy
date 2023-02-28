d = { 'question': "What is machine learning?",
'context': "Machine learning is a subset of artificial intelligence. It is widely for creating a variety of applications such as email filtering and computer vision"
}

import torch
from flask import Flask, request, render_template
model = torch.load('QA')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        text = request.form.get('theirqatext')
        q = request.form.get('theirqas')
        answer = model({'question': q, 'context':text})
        return render_template('qa.html', answer = answer)
    return render_template('qa.html', answer='Your Answer')

app.run(debug=True, host='0.0.0.0', port=8080)
