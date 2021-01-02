from flask import Flask, render_template, make_response
from Forms import RegistrationForm , LoginForm
from flask import request
from flask import Flask, redirect, url_for, request
from firebase import Firebase
import pdfkit

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
firebase = Firebase(config)
db = firebase.database()

data=[]

 

app = Flask(__name__)


app.config['SECRET_KEY']='9fd51d0c027fb09ad5a12825b68b4457'

@app.route('/')
def Home():
    db=firebase.database()
    
    # print(db.child("locations"), "my datasroe")
    # db.child("ProductMovement").push({"timestamp":"Nov 13 2020", "from_location":"nabluse", "to_location":"","product_id":"table", "qyt":165 })
    # data2= db.child("locations").get()
    # print(db.ref())
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


@app.route('/Reports',methods = ['POST', 'GET'])
def PDF_Template():
    render = render_template('pdfReport.html')
    pdf = pdfkit.from_string(render, False)
    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='inline; filename=output.pdf'
    
    return response
    

if __name__ == '__main__':
   app.run(debug = True)