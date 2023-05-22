import datetime
import db
from sqlalchemy import ( Column, Integer, Text, Boolean, DateTime, ForeignKey )
from sqlalchemy.orm import relationship

# Usuarios

class User(db.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    creation_date = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __init__(self, username:str, password:str, admin:bool = False):
        self.username = username
        self.password = password
        self.admin = admin

    def __repr__(self):
        return f"User({self.username, self.admin})"
    
    def __str__(self):
        return self.username
    
# Categorías

class Category(db.Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    parent_id = Column(Integer, ForeignKey("category.id", ondelete="RESTRICT"), nullable=True)
    name = Column(Text, nullable=False)

    def __init__(self, name:str, category_id:int = None):
        self.name = name
        self.category_id = category_id
    
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

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    parent_id = Column(Integer, ForeignKey("entry.id", ondelete="RESTRICT"), nullable=True)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="RESTRICT"), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"), nullable=False)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=True)
    creation_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    last_modified = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __init__(self, user_id:int, title:str, content:str = None, entry_id = None, category_id = None):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.entry_id = entry_id
        self.category_id = category_id
    
    def __repr__(self):
        return f"Entry({self.title[:20]})"
    
    def __str__(self):
        return self.title

# Adjuntos

class Attachment(db.Base):
    __tablename__ = "attachment"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    entry_id = Column(Integer, ForeignKey("entry.id", ondelete="CASCADE"), nullable=False)
    name = Column(Text, nullable=False)
    hash = Column(Text, nullable=False)
    upload_date = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __init__(self, entry_id:int, name:str, hash:str):
        self.entry_id = entry_id
        self.name = name
        self.hash = hash
    
    def __repr__(self):
        return f"Attachment({self.hash})"
    
    def __str__(self):
        return self.name