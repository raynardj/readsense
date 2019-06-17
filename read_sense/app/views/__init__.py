from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, expose

from .. import appbuilder, db
from read_sense.app.views.books_view import bookTextView, authorView, bookView
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
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

from flask_appbuilder.security.registerviews import RegisterUserDBView

class MyRegisterUserDBView(RegisterUserDBView):
    email_template = 'register_mail.html'
    email_subject = 'Your Account activation'
    activation_template = 'activation.html'
    form_title = 'Sing up for free'
    error_message = 'Not possible to register you at the moment, try again later'
    message = 'Registration sent to your email'

appbuilder.add_view(bookTextView,"Book Text",category = "Resources")
appbuilder.add_view(authorView,"Authors",category = "Resources")
appbuilder.add_view(bookView,"Books",category = "Resources")

appbuilder.add_view(MyRegisterUserDBView,"Register")

db.create_all()
