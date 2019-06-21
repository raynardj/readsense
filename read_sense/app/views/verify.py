from flask_appbuilder import BaseView
from flask_appbuilder import expose
from flask import jsonify
from flask import request,redirect
import requests
import json

class verifyView(BaseView):
    route_base = "/verify"

    @expose("/gr/v3/", methods=["POST"])
    def grv3(self):
        rdict = json.loads(request.data)
        token = rdict["token"]
        dt = {"secret":self.appbuilder.app.config["RECAPTCHA_PRIVATE_KEY_V3"],
              "response":token,"remoteip":request.remote_addr
              }
        r = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data=dt
        )
        result = r.json()
        print(result)
        return jsonify(result)