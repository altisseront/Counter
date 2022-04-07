from re import S
from flask import Flask, render_template, request, redirect, session# Import Flask to allow us to create our app
app = Flask(__name__)
app.secret_key = 'chiken'    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/twice')
def twice():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.