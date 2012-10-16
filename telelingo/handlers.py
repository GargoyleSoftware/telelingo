#!/usr/bin/env python

from brubeck.request_handling import Brubeck, WebMessageHandler
from brubeck.connections import Mongrel2Connection

class DemoHandler(WebMessageHandler):
    """
    Hello world.
    """
    def get(self):
        name = self.get_argument('name', 'dude')
        self.set_body('Take six, %s!' % name)
        return self.render()

class InboundEmailHandler(WebMessageHandler):
    """
    Listens for the POST messages coming in from MailGun and puts them in
    the Email Queue.
    Also charges the sending user a fee when the email is received.
    """
    def post(self):
        self.set_body('Take six, %s!' % name)
        return self.render()

class EmailQueueHandler(WebMessageHandler):
    """
    Allows workers to view the mail queue.
    Also allows them to POST an email translation back to the queue.
    """
    def get(self):
        self.set_body('Take six, %s!' % name)
        return self.render()
    def post(self):
      pass

class BuyCreditsHandler(WebMessageHandler):
    """
    UI for purchasing more translation credits.
    """
    def get(self):
        self.set_body('Take six, %s!' % name)
        return self.render()
    def post(self):
        self.set_body('Take six, %s!' % name)
        return self.render()
