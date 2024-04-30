# Integrate HTML with Flask
# HTTP verb GET and POST

# Building URL Dynamically
#Variable Rules and URL Building

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')

def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')

def success(score):
    return f"Passed! \nThe Person score is {score}"

@app.route('/fail/<int:score>')

def fail(score):
    return f"Failed! \nThe Person score is {score}"

@app.route('/results/<int:marks>')

def results(marks):
    result = ""

    if marks < 50:
        result = 'fail'
    else:
        result = 'success'

    return redirect(url_for(result, score = marks)) 
    #Result is basically a URL
    #score is the variable we have defined

# Result Checker HTML page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0

    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science+maths+c+datascience)/4

    res = ""
    if total_score >= 50:
        res = "success"
    else:
        res = 'fail'

    return redirect(url_for(res, score = total_score))


if __name__ == '__main__':
    app.run(debug = True)