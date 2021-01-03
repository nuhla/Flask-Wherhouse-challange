from flask import Flask, render_template, make_response
from Forms import  LocationsForm,ProductForm,UpdateProductForm
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


   
   
# @app.route('/Register',methods = ['POST', 'GET'])
# def Register():
#     form= RegistrationForm()
#     return render_template('register.html', title="Register", form=form )
#     pass

# @app.route('/Login',methods = ['POST', 'GET'])
# def LogIn():
#     form= LoginForm()
#     return render_template('login.html', title="LogIn", form=form )
#     pass

#  ---------------------- Define Our rout of Movment Report -----------------------#
@app.route('/Reports',methods = ['POST', 'GET'])
def PDF_Template():
    # ------------ get all documnts from firebase realtime database ---------------#
    data =  db.child("ProductMovement").get()
    valuesList=[]
    #  ------------------- convert data tuples into a list of dict ----------------#
    for item in data.each() :
        value=db.child("ProductMovement").child(item.key()).get()
        valuesList.append(dict(value.val()))
       
    # ------------- get our html page gived all data to concerted to html tags -------#
    render = render_template('pdfReport.html', data=valuesList)
    # --------- create a string out of our final html page then convert ot to pdf -----#
    pdf = pdfkit.from_string(render, False)
    #------ create our response and response header to viwe the report in the page ----#
    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='inline; filename=output.pdf'
    # ---------------------- send response back to the window --------------------------#
    return response


#  ---------------------- Locations View Add and Edit -----------------------#
@app.route('/Locations',methods = ['POST', 'GET'])
def Add_Remove_View_Locations():
     # ------------ get all documnts from firebase realtime database ---------------#
    data =  db.child("Location").get()
    valuesList=[]
    #  ------------------- convert data tuples into a list of dict ----------------#
    for item in data.each() :
        value=db.child("Location").child(item.key()).get()
        print(value.val())
        val=('key',str(item.key()))
        
     
        var = dict(value.val())
        var['key']=str(item.key())
        valuesList.append(var)
       
        # print(valuesList)
        
    form = LocationsForm(request.form)
    if request.method =='POST' and form.validate():
        location_id = form.location_id.data
        print(location_id, "location_id")
        db.child("Location").push({"location_id":location_id })
        return redirect(request.referrer)


    return render_template("Locations.html", data=valuesList,form=form)


#  ---------------------- Locations View Add and Edit -----------------------#
@app.route('/Product',methods = ['POST', 'GET'])
def Add_View_Product():
     # ------------ get all documnts from firebase realtime database ---------------#
    data =  db.child("Product").get()
    valuesList=[]
   
    #  ------------------- convert data tuples into a list of dict ----------------#
    for item in data.each() :
        value=db.child("Product").child(item.key()).get()
        # print(value.val())
        val=('key',str(item.key()))
        
     
        var = dict(value.val())
        var['key']=str(item.key())
        valuesList.append(var)
        print(valuesList)
        
    form = ProductForm(request.form)
    if request.method =='POST' and form.validate():
        product_id = form.product_id.data
        print(ProductForm, "product_id")
        db.child("Product").push({"product_id":product_id })
        return redirect(request.referrer)


    return render_template("Product.html", data=valuesList,form=form)

#  ---------------------- Locations View Add and Edit -----------------------#
@app.route('/UpdateProduct/<ID>/',methods = ['POST', 'GET'])
def update_Remove_View_Product(ID):
    form = UpdateProductForm(request.form)
    if request.method =='POST':
        product_id = form.product_id.data
        print(request.data, "dddddddddddddddd")
        db.child("Product").child(ID).update({"product_id":product_id})

    return render_template("UpdatProduct.html", form=form , item={'product_id':ID})

if __name__ == '__main__':
   app.run(debug = True)