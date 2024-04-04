from flask import Flask
from src.routes.routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'REGUSER'

app.add_url_rule(routes["indexRoute"], view_func= routes["indexRoute_controller"])
app.add_url_rule(routes["viewRegisteredRoute"], view_func= routes["viewRegistered_controller"])
app.add_url_rule(routes["viewRegisteredRouteSearch"], view_func= routes["viewRegisteredSearch_controller"])