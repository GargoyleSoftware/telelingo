#!/usr/bin/env python

import sys
import os
from datetime import datetime

from brubeck.request_handling import Brubeck
from brubeck.connections import Mongrel2Connection

from util import autoreload

class Command:
    def __init__(self, *args, **options):
        self.stdout = sys.stdout

    def run(self, *args, **options):
        """
        Runs the server, using the autoreloader if needed
        """
        use_reloader = options.get('use_reloader')

        if use_reloader:
            autoreload.main(self.inner_run, args, options)
        else:
            self.inner_run(*args, **options)

    def inner_run(self, *args, **options):
        threading = options.get('use_threading')
        shutdown_message = options.get('shutdown_message', '')
        quit_command = (sys.platform == 'win32') and 'CTRL-BREAK' or 'CONTROL-C'

        try:
            # fire up the app
            from main import run
            run()

        except KeyboardInterrupt:
            if shutdown_message:
                self.stdout.write(shutdown_message)
            sys.exit(0)

if __name__ == '__main__':
    Command().run(use_reloader=True)
