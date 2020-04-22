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
@app.route('/checkTriangle', methods=['GET'])
def checkTriangle():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")
    
    a = int(a)
    b = int(b)
    c = int(c)
    if (a + b > c) and (a + c > b) and (b + c > a):
        kq = " day la tam giac "
        if (a == b) and (b == c):
            kq = kq + "deu"
        else:
            if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
                kq = kq + "vuong"
            if (a == b) or (b == c) or (c == a):
                kq = kq + "can"
    else:
        kq = "khong phai tam giac"      
    return kq
@app.route('/giaiptb2', methods=['GET'])
def giaiptb2():
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
            kq = "Vo nghiem"
        if (k == 0):
            x = -b/(2*a)
            str = "Co 1 nghiem"
            kq = { "tt" : str , "x" : x}
        if (k > 0):
            kq = "Co 2 nghiem"
    else:
        if (b == 0):
            if (c == 0):
                kq = "Vo so nghiem"
            else:
                kq = "Vo nghiem"
        else:
            if (c == 0):
                kq = "Nghiem là 0"
            else:
                x = -c/b
                str = "Nghiem la "
                kq = { "tt" : str , "x" : x}
    return jsonify(kq)
