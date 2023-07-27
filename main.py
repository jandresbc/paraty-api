from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app.Models.database import db
from app.Resources.ReadDataResources import readData
from app.Resources.ViewResources import viewData
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db.init_app(app)
migrate = Migrate(app,db)

api.add_resource(readData,"/read")

api.add_resource(viewData,"/filter")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=Config.DEBUG)