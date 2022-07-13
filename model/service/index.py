from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def login():
    return "首页API"

