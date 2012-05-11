import email
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app

class ChatMailHandler(InboundMailHandler):
	def receive(self, mail_message):
		mail.send_mail(sender="dreher.sebastian@googlemail.com",
		to="bastian.dreher@gmx.net",
		subject="CHAT ADMIN MAIL: %s" % mail_message.subject,
		body="Original message from: %s\n%s" % (mail_message.sender,mail_message.body)

chatmail = webapp.WSGIApplication([InboundMailHandler.mapping()])

def main():
    run_wsgi_app(chatmail)

if __name__ == "__main__":
    main()
