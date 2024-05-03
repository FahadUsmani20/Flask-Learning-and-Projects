# Jinja2 Template Engine
"""
{%. . .%} - For COnditional Statements such as for loops if conditions etc
{{    }} - Expressions to Print Outputs
{#. . .#} - Internal Comments
"""

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route('/') #Home Page
def welcome():
    return render_template('index.html') 

@app.route('/results/<int:marks>') #resuts_jinja Page
def results(marks):
    return render_template('result_jinja.html', grade = marks)

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