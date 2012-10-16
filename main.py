#!/usr/bin/env python

from telelingo.handlers import *
from brubeck.templating import Jinja2Rendering, load_jinja2_env

import runserver

###
### Configuration
###

# Routing config
handler_tuples = [
  (r'^/$', DemoHandler),
]

# Application config
config = {
    'msg_conn': Mongrel2Connection('tcp://127.0.0.1:9999', 'tcp://127.0.0.1:9998'),
    'handler_tuples': handler_tuples,
    'template_loader': load_jinja2_env('./templates/'),
    'api_base_url': '/api/',
}

def run():
  # Instantiate app instance
  app = Brubeck(**config)
  app.run()

if __name__ == '__main__':
  run()
