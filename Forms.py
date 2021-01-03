

from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired,Length, Email



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
    
class LocationsForm(Form):
    location_id =StringField('location',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('add')
    
class ProductForm(Form):
    product_id =StringField('Product',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('add')
    
class UpdateProductForm(Form):
    product_id =StringField('Product',  [validators.Length(min=4, max=25)])
    Submit =SubmitField('Update')
                                           
 