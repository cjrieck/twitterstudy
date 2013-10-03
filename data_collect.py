from twitter import *
from os import *
import oauth2 as oauth
import urlparse

CONSUMER_KEY = 'AuXAERpcZ2i0hprKP60yJw'
CONSUMER_SECRET = 'RDi4O1l8eBcllACuqiY8z1NWXCgrAjowALmR0GXxAZY'


# Trying to automate authentication for any User
def authenticate():
	consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

	request_token_url = 'http://twitter.com/oauth/request_token'
	access_token_url = 'http://api.twitter.com/oauth/access_token'
	authorize_url = 'http://api.twitter.com/oauth/authorize'



	client = oauth.Client(consumer)

	# Get a request token. Temporary token for having the User authorize an access token and
	# sign the request to obtain said access token
	# Found on https://github.com/mkaziz/python-oauth2
	resp, content = client.request(request_token_url, "POST", body="oauth_callback=oob")

	if resp['status'] != 200:
		raise Exception("Invalid response %s." % resp['status'])

	request_token = dict(urlparse.parse_qsl(content))
	print resp
	print request_token
	# print "Request Token:"
	# print "    - oauth_token        = %s" % request_token['oauth_token']
	# print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
	# print


def main():
	pass


if __name__ == '__main__':
	main()