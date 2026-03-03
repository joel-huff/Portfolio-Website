from flask import Flask, render_template, url_for, request
import smtplib
import os
from dotenv import find_dotenv, load_dotenv
from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
@app.route('/')
def home():
    url_for('static', filename='static/images/portfolio-image.png')
    url_for('static', filename='static/style.css')
    url_for('static', filename='static/script.js')
    email_form = EmailForm()
    return render_template("index.html", form=email_form)
#create class for Form
class EmailForm(FlaskForm):
    name = StringField(render_kw={'placeholder': 'First and last name'}, validators=[DataRequired()])
    email = StringField(render_kw={'placeholder': 'example@mail.com'}, validators=[DataRequired(), Email()])
    message = TextAreaField(render_kw={'placeholder': 'Type email here'}, validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField()

@app.route("/contact", methods=['POST'])
def contact():
    # pull info for login from .env file
    dotenv_path = find_dotenv()

    load_dotenv(dotenv_path)
    user_name = os.getenv("EM_UN")
    pswd = os.getenv("EM_UP")
    form = EmailForm(request.form)
    if request.method == "POST" and form.validate():
        #bring in variables from our form
        form_name = str(form['name'].data)
        form_email = str(form['email'].data)
        form_message = str(form['message'].data)

        full_message = (f"Incoming email from {form_name} from email {form_email}\n"
                        f"The email message also follows:\n"
                        f"{form_message}")
        print(full_message)
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

        return render_template('index.html', form=form)
    else:
        print("An error has occurred")



if __name__ == '__main__':
    app.run(debug=True)