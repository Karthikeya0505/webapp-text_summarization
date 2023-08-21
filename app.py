from flask import Flask,render_template,request,redirect,url_for
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/summarize",methods=['POST','GET'])
def summarize():
    if request.method == 'POST':
        data = request.form['data']
        summarizer = pipeline("summarization")
        max_length = int(request.form['max-length'])
        result = summarizer(data,min_length = 5,max_length = max_length)
        try:
            res = result[0]['summary_text']
            length = len(res.split(" "))
        except KeyError as e:
            pass

    return render_template('summary.html',result = res,length = length)

if __name__ == '__main__':
    app.run(debug=True)
