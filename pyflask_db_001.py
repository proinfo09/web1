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
