import flask
from flask import jsonify
from core.subtitles import shift_subtitles_line


web_blueprint = flask.Blueprint('web_blueprint', __name__, template_folder='templates')


@web_blueprint.route("/")
def index():
    return flask.render_template("index.html.jinja2")


@web_blueprint.route("/process_subtitles", methods=["POST"])
def process_subtitles():

    delay_value = float(flask.request.form["delayValue"])
    subtitles_text = flask.request.form["subtitlesText"]

    result = ""
    for line in subtitles_text.split("\n"):
        processed_line = shift_subtitles_line(line, delay_value)
        result += f"{processed_line}\n"

    result = {
        "status": "success",
        "result": result
    }

    return jsonify(result)
