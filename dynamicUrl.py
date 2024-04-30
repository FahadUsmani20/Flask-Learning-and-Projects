# Building URL Dynamically
#Variable Rules and URL Building

from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.route('/')

def welcome():
    return "welcome"

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


if __name__ == '__main__':
    app.run(debug = True)