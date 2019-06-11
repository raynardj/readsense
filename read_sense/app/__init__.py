import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA, expose
from flask_appbuilder import IndexView
import pandas as pd
from collections import namedtuple
import random

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)

author_ = namedtuple("author",["id","name"])
book_ = namedtuple("book",["id","name"])

authordf = pd.read_sql("authors",con=db.engine)
booksdf = pd.read_sql("books", con=db.engine)
authors = list(author_(i, a) for i, a in zip(authordf["index"],authordf.author))
books = list(book_(i,b) for i, b in zip(booksdf["book_id"], booksdf.bookname))

class CustomeIndexView(IndexView):

    index_template = "index.html"
    route_base = "/"

    @expose("/")
    def index(self):
        author_choice = random.sample(authors,20)
        book_choice = random.sample(books,30)
        return self.render_template("index.html",author_choice = author_choice,book_choice=book_choice)

appbuilder = AppBuilder(app, db.session, indexview=CustomeIndexView)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
