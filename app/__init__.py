from flask import Flask
from flask_cors import CORS
from app.controller import accountController

app = Flask(__name__)

CORS(app)
app.register_blueprint(accountController.api_account)