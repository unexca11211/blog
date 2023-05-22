import db
from models import Entry
from flask import ( Blueprint, request )

bp = Blueprint("Entry", __name__, url_prefix="/entry")

@bp.before_request
def before_request():
    # TODO: Validar sesión
    pass