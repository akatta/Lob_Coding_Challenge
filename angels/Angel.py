import api
import sys

"""Object that represents a part of result from Angel List. Can be a user, startup, LocationTag, etc.
	Takes in a dictionary of features."""

class Angel(object):
	def __init__(self, dic = {}):
		self.dic = dic
		self.api = api.AngelList()

	def get(self, key):
		try:
			val = self.dic[key]
		except KeyError:
			raise self.api.AngelListError("Key does not exist")
		if isinstance(val, list) and all(isinstance(x, dict) for x in val):
			return [Angel(x) for x in val]
		elif isinstance(val, dict):
			return Angel(val)
		else:
			return val



