# Integrate HTML with Flask
# HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template, request

#render template requires a template folder to work
#requests is used to get data from pages

app = Flask(__name__)

@app.route('/') #Home Page
def welcome():
    return render_template('index.html') 

@app.route('/results/<int:marks>') #Results Page
def results(marks):
    res = ""

    if marks < 50:
        res = 'Failed'
    else:
        res = 'Passed'
    
    return render_template('result.html', grade = res)
    #grade = res // grade is the value in result.html 

# Result Checker HTML page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():

    if request.method == 'POST':
        
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science+maths+c+datascience)/4


    return redirect(url_for("results", marks = total_score))


if __name__ == '__main__':
    app.run(debug = True)