from flask import Flask, render_template
from Forms import RegistrationForm , LoginForm
from flask import request
from flask import Flask, redirect, url_for, request
import pyrebase

config = {
    "apiKey": "AIzaSyC_16qNyYweahPpI08fq5PU4scSTSkmwT4",
  "authDomain": "challange-nuhla.firebaseapp.com",
  "databaseURL": "https://challange-nuhla.firebaseio.com",
  "projectId": "challange-nuhla",
  "storageBucket": "challange-nuhla.appspot.com",
  "messagingSenderId": "36855175985",
  "appId": "1:36855175985:web:e8f30719f027fe2234ee10",
  "measurementId": "G-PS94E533ME"
}
firebase = pyrebase.initialize_app(config)
db=firebase.database()
print(db.get())

data=[]

 

app = Flask(__name__)


app.config['SECRET_KEY']='9fd51d0c027fb09ad5a12825b68b4457'

@app.route('/')
def Home():
    return render_template('HomePage.html', data=data, title="homepage")
def hello_world():
    return 'Hello, World!'

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#     pass
# #    if request.method == 'POST':
# #       user = request.form['name']
# #       return redirect(url_for('dashboard',name = user))
# #    else:
# #       user = request.args.get('name')
# #       return render_template('login.html')


   
   
@app.route('/Register',methods = ['POST', 'GET'])
def Register():
    form= RegistrationForm()
    return render_template('register.html', title="Register", form=form )
    pass

@app.route('/Login',methods = ['POST', 'GET'])
def LogIn():
    form= LoginForm()
    return render_template('login.html', title="LogIn", form=form )
    pass

if __name__ == '__main__':
   app.run(debug = True)