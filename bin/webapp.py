import flask
import os
from core.blueprints.web_blueprint import web_blueprint

location_webfolder = None
for location_candidate in ["../../webfolder", "../webfolder", "webfolder"]:
    if os.path.exists(location_candidate):
        location_webfolder = os.path.abspath(location_candidate)


app = flask.Flask(__name__, template_folder=f"{location_webfolder}/templates", static_folder=f"{location_webfolder}/assets")

app.register_blueprint(web_blueprint)
