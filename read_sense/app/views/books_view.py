from flask_appbuilder import ModelView, expose
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface

from read_sense.app.models.books import bookDoc,authorModel, bookModel

class bookTextView(ModelView):
    datamodel = SQLAInterface(bookDoc)
    route_base = "/booktext"

    list_columns = ["index","books","fmt","maps"]

class authorView(ModelView):
    datamodel = SQLAInterface(authorModel)
    route_base = "/author"

    label_columns = {"author":"Auther Name","born":"Year of Birth","death":"Year of Decease"}
    list_columns = ["author","born_year","death_year"]
    list_title = "Authors"
    show_title = "Author Detail"
    edit_title = "Change Author Info"
    add_title = "Create New Author"

class bookView(ModelView):
    datamodel = SQLAInterface(bookModel)
    route_base = "/book"
    label_columns = {"bookname":"Book Name","cate1":"Category","readbook":"Read"}

    list_columns = ["bookname","author","cate1","readbook"]
    show_columns = ["bookname","author","chapters","readbook"]
    list_title = "Books"
    show_title = "Book Detail"
    edit_title = "Edit Book Detail"
    add_title = "Add a New Book"

    @expose("/readbook/<book_id>/")
    def read_book(self,book_id):
        book = self.datamodel.get(book_id)
        return self.render_template("readbook.html", book = book)