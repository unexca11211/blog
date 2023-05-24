import datetime
import db
import uuid
from sqlalchemy import ( Column, Uuid, Text, Boolean, TIMESTAMP, ForeignKey )
from sqlalchemy.orm import relationship

# Usuarios

class User(db.Base):
    __tablename__ = "user"

    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    def __init__(self, username:str, password:str, email:str, is_admin:bool = False):
        self.username = username
        self.password = password
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return f"User({self.username, self.admin})"
    
    def __str__(self):
        return self.username
    
# Categorías

class Category(db.Base):
    __tablename__ = "category"

    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    parent_id = Column(Uuid, ForeignKey("category.id", ondelete="RESTRICT"), nullable=True)
    name = Column(Text, nullable=False)

    def __init__(self, name:str, parent_id = None):
        self.name = name
        self.parent_id = parent_id
    
    def __repr__(self):
        return f"Category({self.name[:20]})"
    
    def __str__(self):
        return self.name
    
    def parent(self):
        return None if self.parent_id is None else db.session.query(Category).where(Category.id == self.parent_id).first()
    
    def children(self):
        return db.session.query(Category).where(Category.parent_id == self.id).all()

# Entradas

class Entry(db.Base):
    __tablename__ = "entry"

    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    parent_id = Column(Uuid, ForeignKey("entry.id", ondelete="RESTRICT"), nullable=True)
    category_id = Column(Uuid, ForeignKey("category.id", ondelete="RESTRICT"), nullable=True)
    user_id = Column(Uuid, ForeignKey("user.id", ondelete="RESTRICT"), nullable=False)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)

    def __init__(self, user_id, title:str, content:str = None, parent_id = None, category_id = None):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.parent_id = parent_id
        self.category_id = category_id
    
    def __repr__(self):
        return f"Entry({self.title[:20]})"
    
    def __str__(self):
        return self.title

# Adjuntos

class Attachment(db.Base):
    __tablename__ = "attachment"

    id = Column(Uuid, primary_key=True, nullable=False, default=uuid.uuid4)
    entry_id = Column(Uuid, ForeignKey("entry.id", ondelete="CASCADE"), nullable=False)
    name = Column(Text, nullable=False)
    hash = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)

    def __init__(self, entry_id, name:str, hash:str):
        self.entry_id = entry_id
        self.name = name
        self.hash = hash
    
    def __repr__(self):
        return f"Attachment({self.hash})"
    
    def __str__(self):
        return self.name