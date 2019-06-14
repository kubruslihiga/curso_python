from flask import Blueprint
from flask import jsonify


usr = Blueprint("user", __name__)


@usr.route("/api/usr")
def index():
    resposta = {"success": "ok"}
    return jsonify(resposta)
