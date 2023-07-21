from flask import render_template,  Flask, request
from summary_generator import summary_generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods = ['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext= request.form['Raw_text']
        summary, original_text, len_original, len_summary = summary_generator(rawtext)

    return render_template('summary.html', original_text=original_text, summary = summary, len_original=len_original, len_summary=len_summary)

if __name__ == '__main__':
    app.run(debug=True)
