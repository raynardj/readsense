# A Classical Literature Library
### With many nlp techniques applied to it

## Installation
### Requirements
Install the following python lib under your environment
```
flask
flask_appbuilder
flask_mail
pandas
requests
gunicorn
```

### Write a configuration file for google reCAPTCHA and website email, in following format

The configuration file shall be stored in ```/etc/rasenn.cfg```

```cfg

[Email]
mail_username = abc@gmail.com
mail_password = thisIsMailPassw0rd
mail_use_tls = True
mail_server = smtp.somemail.com
mail_default_sender = abc@gmail.com

[reC]
recaptcha_public_key = xxxxxxxxxxxxxxxxxxxxxxxx
recaptcha_private_key = zzzzzzzzzzzzzzzzzzzzzzzz

[reC_v3]
recaptcha_public_key_v3 = xxxxxxxxxxxxxxxxxxxxxxxx
recaptcha_private_key_v3 = zzzzzzzzzzzzzzzzzzzzzzzz

```

### Logging
When constructing view function:
```python
from flask_appbuilder import expose
from readsense.utils import log_writer
@expose("/somepath/", methods=["GET"])
@log_writer
def something(self):
    somecode = somecode
    return self.render_template("some_template.html")
```

### Redirecting the port
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

