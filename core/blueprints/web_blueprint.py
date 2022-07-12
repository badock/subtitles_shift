import flask
from flask import jsonify
from core.subtitles import shift_subtitles_line
from core.config import get_options


web_blueprint = flask.Blueprint('web_blueprint', __name__, template_folder='templates')


@web_blueprint.route("/")
def index():
    options = get_options()

    adsense_code = options.get("shiftsubs").get("adsense")
    # return flask.render_template("index.html.jinja2", adsense_code=adsense_code)
    return flask.render_template("index_single_file.html.jinja2", adsense_code=adsense_code)


@web_blueprint.route("/help")
def help():
    options = get_options()

    adsense_code = options.get("shiftsubs").get("adsense")
    return flask.render_template("help.html.jinja2", adsense_code=adsense_code)


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
