# A Classical Literature Library
### With many nlp techniques applied to it

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

```