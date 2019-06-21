from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, expose

from .. import appbuilder, db
from read_sense.app.views.books_view import bookTextView, authorView, bookView
from read_sense.app.views.jsviews import JSView
from read_sense.app.views.verify import verifyView
from flask import redirect,flash
import pandas as pd

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    flash("We have restructured our website, try and search the book you want by the following search box","danger")
    return redirect("/")



appbuilder.add_view(bookTextView,"Book Text",category = "Resources")
appbuilder.add_view(authorView,"Authors",category = "Resources")
appbuilder.add_view(bookView,"Books",category = "Resources")
appbuilder.add_view_no_menu(JSView)
appbuilder.add_view_no_menu(verifyView)

# appbuilder.add_view(MyRegisterUserDBView,"Register")

db.create_all()
