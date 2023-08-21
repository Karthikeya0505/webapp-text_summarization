from flask import Flask,render_template,request,redirect,url_for
from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/summarize",methods=['POST','GET'])
def summarize():
    if request.method == 'POST':
        data = request.form['data']
        summarizer = pipeline("summarization",model="facebook/bart-large-cnn")
        #max_length = int(request.form['max-length'])
        result = summarizer(data,min_length = 5)
        try:
            res = result[0]['summary_text']
            length = len(res.split(" "))
        except KeyError as e:
            pass

    return render_template('index.html',result = res)

if __name__ == '__main__':
    app.run(debug=True)
