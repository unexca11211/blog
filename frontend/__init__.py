from flask import ( Blueprint, send_from_directory )
from frontend import Attachment

bp = Blueprint("Frontend", __name__, url_prefix="/")

bp.register_blueprint(Attachment.bp)

@bp.route("/")
def serveIndex():
    return serveSite("index.html")

@bp.route("/<path:path>")
def serveSite(path:str):
    return send_from_directory('frontend/web', path)

@bp.errorhandler(404)
def itemNotFound(err):
    return serveSite("404.html")