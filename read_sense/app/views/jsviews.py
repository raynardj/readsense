from flask_appbuilder import BaseView
from flask_appbuilder import expose

class JSView(BaseView):
    route_base = "/jsrender"

    @expose("/grecaptcha/v3/")
    def grecaptchav3(self):
        rec_key_v3 = self.appbuilder.app.config["RECAPTCHA_PUBLIC_KEY_V3"]
        return self.render_template("grecaptcha_v3.js",rec_key_v3 = rec_key_v3)