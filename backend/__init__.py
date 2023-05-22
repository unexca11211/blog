from backend import ( Category )
from flask import ( Blueprint )

bp = Blueprint("API", __name__, url_prefix="/api")

bp.register_blueprint(Category.bp)

@bp.route("/")
def test():
    return { "version": 1 }

@bp.route("/<path:path>")
def invalidRoute(path):
    return { }, 404