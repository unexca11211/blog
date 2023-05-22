import backend
import db
import frontend
from flask import Flask
from flask.json.provider import DefaultJSONProvider
from models import User

db.Base.metadata.create_all(db.engine)

app = Flask(__name__)
app.register_blueprint(backend.bp)
app.register_blueprint(frontend.bp)

DefaultJSONProvider.sort_keys = False