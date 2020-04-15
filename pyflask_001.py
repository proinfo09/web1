from flask import  (
    Flask,
    render_template
)

app = Flask(__name__)

@app.route('/')
def  index():
    return "<h1> Tu Duong Hieu - Hi </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")
