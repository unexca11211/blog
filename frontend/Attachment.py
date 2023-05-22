import db
from flask import ( Blueprint, send_file )
from models import ( Attachment )

bp = Blueprint("Attachment", __name__, url_prefix="/attachment")

@bp.route("/<hash>", methods=["GET"])
def test(hash:str):
    attachment = db.session.query(Attachment).where(Attachment.hash == hash).first()

    if attachment is None:
        return { }, 404
    
    return send_file(f"frontend/attachment/{hash}", download_name=attachment.name)