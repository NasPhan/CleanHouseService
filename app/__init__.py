from flask import Flask
from flask_cors import CORS
from app.controller import accountController
from app.controller import userController
from app.controller import requestController
from app.controller import requestDetailController

app = Flask(__name__)

CORS(app)
app.register_blueprint(accountController.api_account)
app.register_blueprint(userController.api_user) 
app.register_blueprint(requestController.api_request)
app.register_blueprint(requestDetailController.api_requestDetail)