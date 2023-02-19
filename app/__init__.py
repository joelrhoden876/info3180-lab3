from flask import Flask
from flask_mail import Mail
from .config import Config #7

app = Flask(__name__)
app.config.from_object(Config)


app.config['SECRET_KEY'] = 'b_5#y2LF4Q8znxec]/'
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0768f3c7cb8a08'
app.config['MAIL_PASSWORD'] = 'd61b8ea677eb40'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False



mail = Mail(app)
from app import views