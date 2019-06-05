from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from . import db

class bookDoc(Model):
    __tablename__ = "text_files"
    index = db.Column(db.Integer, primary_key=True)
    fmt = db.Column(db.Text())
    text = db.Column(db.Text())

    def __repr__(self):
        return "book file:%s"%(self.index)

class authorModel(Model):
    __tablename__ = "authors"
    index = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Text())
    born = db.Column(db.Integer())
    death = db.Column(db.Integer())

    def __repr__(self):
        return self.author

    @property
    def born_year(self):
        if self.born < 9999:
            return self.born
        else:
            return "No Record"

    @property
    def death_year(self):
        if self.death < 9999:
            return self.death
        else:
            return "No Record"

class bookModel(Model):
    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.Text())
    author_id = db.Column(db.Integer(), db.ForeignKey("authors.index"))
    author = db.relationship(authorModel)
    cate1 = db.Column(db.Text())

    def __repr__(self):
        return self.bookname

    @property
    def readbook(self):
        return "<a class='btn' href='/book/readbook/%s/'>"%(self.book_id)

class bookMap(Model):
    __tablename__ = "book_file"
    index = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    book = db.relationship(bookModel)
    file_id = db.Column(db.Integer, db.ForeignKey("text_files.index"))
    file = db.relationship(bookDoc)
    chapter = db.Column(db.Text())

    def __repr__(self):
        return "Book:%s with File:%s, Chapter:%s"%(self.book,self.file,self.chapter)

bookModel.chapters = db.relationship(bookMap)
bookDoc.books = db.relationship(bookModel, secondary = "book_file")
bookDoc.maps = db.relationship(bookMap)
authorModel.books = db.relationship(bookModel)