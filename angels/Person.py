from Angel import Angel

"""Child class of Angel that represents a person"""

class Person(Angel):

	def getInterests(self):
		interests = self.get("interests")
		# return [x.replace(" ", "%20") for x in interests]
		return interests

	def getAreas(self):
		areas = self.get("areas")
		# return [x.replace(" ", "%20") for x in areas]
		return areas