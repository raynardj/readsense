from flask_appbuilder import ModelView, expose
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface

from read_sense.app.models.books import bookDoc, authorModel, bookModel, bookMap
from read_sense.utils import log_writer
from flask import request
from flask_login import current_user


class bookTextView(ModelView):
    datamodel = SQLAInterface(bookDoc)
    route_base = "/booktext"

    list_columns = ["index", "books", "fmt", "maps"]


class authorView(ModelView):
    datamodel = SQLAInterface(authorModel)
    route_base = "/author"

    label_columns = {"author": "Auther Name", "born": "Year of Birth", "death": "Year of Decease"}
    list_columns = ["author", "born_year", "death_year"]
    show_columns = ["author", "born", "death", "books"]
    list_title = "Authors"
    show_title = "Author Detail"
    edit_title = "Change Author Info"
    add_title = "Create New Author"

    show_template = "author_show.html"

    @expose("/visit/<author_id>/")
    @log_writer
    def visit_author(self, author_id):

        author = self.datamodel.get(int(author_id))
        rec_key_v3 = self.appbuilder.app.config["RECAPTCHA_PUBLIC_KEY_V3"]
        return self.render_template("author_visit.html", author=author,
                                    rec_key_v3=rec_key_v3, action="authorVisit")


class bookView(ModelView):
    datamodel = SQLAInterface(bookModel)
    route_base = "/book"
    label_columns = {"bookname": "Book Name", "cate1": "Category", "readbook": "Read"}

    list_columns = ["bookname", "author", "cate1", "readbook"]
    show_columns = ["bookname", "author", "chapters", "readbook"]
    list_title = "Books"
    show_title = "Book Detail"
    edit_title = "Edit Book Detail"
    add_title = "Add a New Book"

    @expose("/readbook/<book_id>/")
    @log_writer
    def read_book(self, book_id):
        book = self.datamodel.get(book_id)
        rec_key_v3 = self.appbuilder.app.config["RECAPTCHA_PUBLIC_KEY_V3"]
        return self.render_template("readbook.html", book=book,
                                    rec_key_v3=rec_key_v3, action="bookRead")

    @expose("/readchapter/<book_id>/<file_id>/")
    @log_writer
    def read_chapter(self, book_id, file_id):
        book_id = int(book_id)
        file_id = int(file_id)
        book = self.datamodel.get(book_id)
        chapters = book.chapters
        file_ids = list(chapter.file_id for chapter in chapters)
        rec_key_v3 = self.appbuilder.app.config["RECAPTCHA_PUBLIC_KEY_V3"]
        if int(file_id) in file_ids:
            file = chapters[file_ids.index(file_id)].file
            return self.render_template("readbook.html", book=book,
                                        file=file, file_id=file_id,
                                        rec_key_v3=rec_key_v3, action="chapterRead")
        else:
            return self.render_template("readbook.html", book=book,
                                        rec_key_v3=rec_key_v3, action="chapterRead")
