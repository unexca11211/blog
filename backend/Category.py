import db
from models import Category
from flask import ( Blueprint, request )

bp = Blueprint("Category", __name__, url_prefix="/category")

@bp.before_request
def before_request():
    # TODO: Validar sesión
    pass

# Obtiene todas las categorías principales y sus respectivos hijos. No obtiene hijos de los hijos y mas allá.

@bp.route("/", methods=["GET"])
def getCategoryTree():
    categories = db.session.query(Category).where(Category.parent_id == None).all()

    return [
        {
            "id": category.id,
            "name": category.name,
            "children": [ { "id": child.id, "name": child.name } for child in category.children() ]
        } for category in categories
    ]

# Obtiene una categoría en específico

@bp.route("/<int:id>", methods=["GET"])
def getCategory(id:int):
    category = db.session.query(Category).where(Category.id == id).first()

    if category is None:
        return { }, 404
    
    parent = category.parent()
    children = category.children()

    return {
        "id": category.id,
        "name": category.name,
        "parent": None if parent is None else { "id": parent.id, "name": parent.name },
        "children": [ { "id": child.id, "name": child.name } for child in children ]
    }

# Modifica la categoría. Requiere el nombre nuevo

@bp.route("/<int:id>", methods=["POST"])
def modifyCategory(id:int):
    if "name" not in request.form or not request.form["name"]:
        return { }, 400
    
    db.session.query(Category).where(Category.id == id).update({ Category.name: request.form["name"] })

    return { }

# Elimina la categoría

@bp.route("/<int:id>", methods=["DELETE"])
def deleteCategory(id:int):
    db.session.query(Category).where(Category.id == id).delete()

    return { }