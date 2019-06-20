from flask import request
from flask_login import current_user
def log_writer(f):
    def wraps(self,*args,**kwargs):
        request_dt = dict()
        request_dt.update({
            "path": request.url,
            "remote_ip": request.remote_addr,
            # "environ": request.environ,
            "method": request.method,
        })
        if current_user.is_authenticated:
            request_dt.update({"user": current_user.id})
        print(request_dt)
        return f(self,*args,**kwargs)

    return wraps