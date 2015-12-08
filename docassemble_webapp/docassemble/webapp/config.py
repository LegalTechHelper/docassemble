import yaml
import os
import sys

daconfig = dict()

def load(**kwargs):
    global daconfig
    filename = kwargs.get('filename', '/usr/share/docassemble/config.yml')
    if not os.path.isfile(filename):
        if not os.access(os.path.dirname(filename), os.W_OK):
            sys.stderr.write("Configuration file " + str(filename) + " does not exist and cannot be created\n")
            sys.exit(1)
        with open(filename, 'w') as config_file:
            config_file.write(default_config())
            sys.stderr.write("Wrote configuration file to " + str(filename) + "\n")
    if not os.path.isfile(filename):
        sys.stderr.write("Configuration file " + str(filename) + " does not exist\n")
    with open(filename, 'rU') as stream:
        daconfig = yaml.load(stream)
    if daconfig is None:
        sys.stderr.write("Could not open configuration file from " + str(filename) + "\n")
        with open(filename, 'r') as fp:
            sys.stderr.write(fp.read() + "\n")
        sys.exit(1)
    else:
        daconfig['config_file'] = filename
    return

def default_config():
    config = """\
debug: true
root: /
exitpage: /
db:
  prefix: postgresql+psycopg2://
  name: docassemble
  user: null
  password: null
  host: null
  port: null
secretkey: 28asflwjeifwlfjsd2fejfiefw3g4o87
appname: docassemble
brandname: demo
packagecache: /tmp/docassemble-cache
uploads: /usr/share/docassemble/files
packages: /usr/share/docassemble/local
webapp: /usr/share/docassemble/webapp/docassemble.wsgi
mail:
  default_sender: '"Administrator" <no-reply@example.com>'
admin_address: '"Administrator" <admin@example.com>'
use_progress_bar: false
imagemagick: convert
pacpl: pacpl
avconv: avconv
default_interview: docassemble.demo:data/questions/questions.yml
flask_log: /tmp/flask.log
language: en
locale: en_US.utf8
default_admin_account:
  nickname: admin
  email: admin@admin.com
  password: password
"""
    return config
