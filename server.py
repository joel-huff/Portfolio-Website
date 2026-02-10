from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    url_for('static', filename='static/images/portfolio-image.png')
    url_for('static', filename='static/style.css')
    url_for('static', filename='static/script.js')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)