from flask import Flask, render_template, url_for, request
import smtplib
import os
from dotenv import find_dotenv, load_dotenv
from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/')
def home():
    url_for('static', filename='static/images/portfolio-image.png')
    url_for('static', filename='static/style.css')
    url_for('static', filename='static/script.js')
    return render_template("index.html")

@app.route("/contact", methods=['POST'])
def contact():
    # pull info for login from .env file
    dotenv_path = find_dotenv()

    load_dotenv(dotenv_path)
    user_name = os.getenv("EM_UN")
    pswd = os.getenv("EM_UP")

    #bring in variables from our form
    name = request.form['name']
    cname = request.form['cname']
    email = request.form['email']
    pnumber = request.form['pnumber']
    message = request.form['message']

    full_message = (f"Incoming email from {name} from email {email}\n"
                    f"Optional info is as follows: Company name {cname} phone number {pnumber}\n"
                    f"The email message also follows:\n"
                    f"{message}")

    #create email message with formatting
    msg = EmailMessage()
    msg['Subject'] = "Website Inquiry"
    msg['From'] = user_name
    msg['To'] = user_name
    msg.set_content(full_message)

    output = "Confirmed receipt of your email!"
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user_name, pswd)
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent")
    if not name or not email or not message:
        error_message = "Name, email, and a message is required to send an inquiry."
        return
    return render_template("index.html", name=name, cname=cname, email=email, pnumber=pnumber, message=message)
#create secret key


if __name__ == '__main__':
    app.run(debug=True)