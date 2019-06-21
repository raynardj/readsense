import logging
from flask import Flask, request, jsonify
from flask_appbuilder import AppBuilder, SQLA, expose
from flask_appbuilder import IndexView, BaseView
import pandas as pd
from collections import namedtuple
import random
import json
from read_sense import config

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object(config)
db = SQLA(app)

author_ = namedtuple("author", ["id", "name"])
book_ = namedtuple("book", ["id", "name"])

authordf = pd.read_sql("authors", con=db.engine)
booksdf = pd.read_sql("books", con=db.engine)

authordf["author_l"] = authordf.author.apply(lambda x: str(x).lower())
booksdf["bookname_l"] = booksdf.bookname.apply(lambda x: str(x).lower())

authors = list(author_(i, a) for i, a in zip(authordf["index"], authordf.author))
books = list(book_(i, b) for i, b in zip(booksdf["book_id"], booksdf.bookname))


class CustomeIndexView(IndexView):
    index_template = "index.html"
    route_base = "/"

    @expose("/")
    def index(self):
        author_choice = random.sample(authors, 20)
        book_choice = random.sample(books, 30)
        rec_key_v3 = self.appbuilder.app.config["RECAPTCHA_PUBLIC_KEY_V3"]
        return self.render_template("index.html", rec_key_v3 = rec_key_v3,
                                    author_choice=author_choice, book_choice=book_choice)


class searchAPI(BaseView):
    route_base = "/search"

    @expose("/book/", methods=["POST"])
    def search_book(self):
        search_dict = json.loads(request.data)
        kw = str(search_dict["kw"]).lower()
        book_result = booksdf[booksdf.bookname_l.str.contains(kw)].to_dict(orient="index")

        return jsonify(book_result)

    @expose("/author/", methods=["POST"])
    def search_author(self):
        search_dict = json.loads(request.data)
        kw = str(search_dict["kw"]).lower()
        author_result = authordf[authordf.author_l.str.contains(kw)].to_dict(orient="index")

        return jsonify(author_result)

from flask_appbuilder.security.manager import RegisterUserDBView
from flask_appbuilder.security.sqla.manager import SecurityManager


class MyRegisterUserDBView(RegisterUserDBView):
    email_template = 'register_mail.html'
    email_subject = 'Your Account activation'
    activation_template = 'activation.html'
    form_title = 'Sing up for free'
    error_message = 'Not possible to register you at the moment, try again later'
    message = 'Registration sent to your email'

class MySecurityManager(SecurityManager):
    registeruserdbview = MyRegisterUserDBView


appbuilder = AppBuilder(app, db.session, indexview=CustomeIndexView,
                        security_manager_class=MySecurityManager)
appbuilder.add_view_no_menu(searchAPI)

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
