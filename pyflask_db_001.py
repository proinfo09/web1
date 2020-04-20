from flask import  (
    Flask,
    render_template,
    request
)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify


app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

@app.route('/')
def  index():
    return "<h1> Flask DB 001 - Connecting !!! </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")

@app.route('/params', methods=['GET'])
def api_filter():
    query_parameters = request.args
    return jsonify(query_parameters)

class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam

api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1

@app.route('/giaiptb1', methods=['GET'])
def giaiptb1():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")
    
    a = int(a)
    b = int(b)
    c = int(c)
    if (a != 0):
        k = b*b -4*a*c
        if (k < 0):
            kq = "Vô nghiệm"
        if (k == 0):
            kq = "Có 1 nghiệm"
        if (k > 0):
            kq = "Có 2 nghiệm"
    else:
        if (b == 0):
            if (c == 0):
                kq = "Vô số nghiệm"
            else:
                kq = "Vô nghiệm"
        else:
            if (c == 0):
                kq = "Nghiệm là 0"
            else:
                kq = "Có 1 nghiệm"   
    return kq
