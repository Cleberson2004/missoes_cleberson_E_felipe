from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud4.db'
db = SQLAlchemy(app)
from app.models.Mission import Mission
with app.app_context():
    db.create_all()

from app.view.reso_mission import Index, MissionCreate, MissionUpdate, MissionDelete
api.add_resource(Index, '/') #como se fosse a rota, so que com a chamada da api
api.add_resource(MissionCreate, '/criar')
api.add_resource(MissionUpdate, '/atualizar')
api.add_resource(MissionDelete, '/deletar')


'''@app.route("/")
def index():
    #return "<h1> Minha Aplicação em Flask</h1>"
    return render_template("index.html")'''