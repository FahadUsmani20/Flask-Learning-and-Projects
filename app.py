from flask import Flask

app = Flask(__name__)

@app.route('/')

def welcome(): #Defining function immediately after decorators causes the function to be executed as soon as decorator is called
    return "Welcome Fahad, this is amazing"

@app.route('/members')

def members(): #Defining function immediately after decorators causes the function to be executed as soon as decorator is called
    return "Welcome Members, nice to meet you"


if __name__ == '__main__':
    app.run(debug = True)
