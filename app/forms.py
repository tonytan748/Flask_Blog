from flask.ext.wtf import Form
from wtforms import TextField,BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	openid=TextField('openid',validators=[Required()])
	remembar_me=BooleanField('remembar_me',default=False)

