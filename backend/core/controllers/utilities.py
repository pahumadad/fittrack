from flask import Blueprint
from flask.json import jsonify

utilities = Blueprint("utilities", __name__)


@utilities.route("/api/heartbeat/", methods=["GET"])
def heartbeat_state():
    return jsonify({"status": "OK"}), 200
