

from wtforms import Form,DateTimeField, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField
from wtforms.validators import DataRequired,Length, Email
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.fields import html5 as h5fields



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25),validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(),validators.Email(),])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    Submit =SubmitField('Sign Up')
    
    
class LoginForm(Form):
  
    email = StringField('Email', [validators.DataRequired(),validators.Email(),])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    remember = BooleanField('Remember Me')
    Submit =SubmitField('login')
    
    
 #  -------------- the view and ADD location Form -------------------    
class LocationsForm(Form):
    location_id =StringField('location',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('add')
    
#  -------------- the view and ADD Product Form -------------
class ProductForm(Form):
    product_id =StringField('Product',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('add')
#  -------------- the Product update Form -------------------   
class UpdateProductForm(Form):
    product_id =StringField('Product',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('Update')
    
#  -------------- the Location update Form -------------------   
class UpdateLocationsForm(Form):
    location_id =StringField('Location',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('Update')
    
#  -------------- the Movments update Form -------------------   
class MovmentsForm(Form):
    from_location =SelectField('Location',  choices=[])
    to_location =SelectField('Location',  choices=[])
    product_id =SelectField('Product',  choices=[])
    timestamp =DateTimeLocalField('Time', format='%m/%d/%y')
    qyt=h5fields.IntegerField(
        "Number2"
    )

    # qyt=h5fields
    Submit =SubmitField('Add')
                                           
 