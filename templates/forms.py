from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import data_required,length,email,EqualTo

class register(FlaskForm):
    username=StringField('Username',validators=[data_required(),length(min=2,max=20)])
    email=StringField("email",validators=[data_required(),email()])
    password=PasswordField("password",validators=[data_required()])
    confirm_pass=PasswordField('confirm pass',validators=[data_required(), EqualTo('password')])
    submit=SubmitField("sign_up")