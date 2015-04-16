import hashlib
import urllib, urllib2
import os
try:
	import simplejson as json
except ImportError:
	import json


""" Python adaptation of Angel List API"""
class AngelListError(Exception):

  def __init__(self, value):
    self.parameter = value

  def __str__(self):
    return repr(self.parameter)

class AngelList(object):
	def __init__(self, token=None):
		self.prefix = "https://"
		self.API_ENDPOINT = "api.angel.co/1/"
		get_token = os.getenv("ANGEL_ACCESS_TOKEN")
		""" Will try to get access token from your machine"""
		# self.accesstoken = token if token else "cc65af5a8fd1f408c8d1ba0bf1c18e4d55c84278fc6575b4"
		self.accesstoken = get_token if get_token else token
		if not self.accesstoken:
			print "Please pass in valid access token"


	def do_get_request(self, request, queries=None):
		query = ''
		if queries:
			for q in queries.keys():
				s = "{0}={1}&".format(str(q),queries[q])
				query += s
		auth = "access_token={0}".format(self.accesstoken)
		url = "{0}{1}{2}?{3}{4}".format(self.prefix, self.API_ENDPOINT, request, query, auth)
		url = urllib.quote(url)
		response = urllib2.urlopen(url)
		return json.loads(response.read())

	def do_post_request(self, request, queries=None, data=None):
		query = ''
		if queries:
			for q in queries.keys():
				s = str(q) + "=" + queries[q] + "&"
				query += s
		auth = "access_token=" + self.accesstoken
		url = "{0}{1}{2}?{3}{4}".format(self.prefix, self.API_ENDPOINT, request, query, auth)
		url = urllib.quote(url)
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		params = urllib.urlencode(data)
		response = urllib2.urlopen(urllib2.Request(url, params, headers))
		return json.loads(response.read())