from Angel import Angel

"""Child class of Angel that represents a startup"""

class Startup(Angel):

	def getLocation(self):
		location_objects = self.get("locations")
		places = []
		for loc in location_objects:
			places.append(loc.get("display_name"))
		return places

	def hidden(self):
		return self.get("hidden")

	def getMarkets(self):
		market_objects = self.get("markets")
		markets = []
		for mark in market_objects:
			markets.append(mark.get("name"))
		return markets

	def getJobs(self):
		return self.api.do_get_request("startups/{0}/jobs".format(self.get("id")))

	def printInfo(self):
		parameters = ["Name", "Locations", "Quality", "Markets", "Website"]
		info = [self.get('name'), self.getLocation(), self.get('quality'), self.getMarkets(), self.get("company_url")]

		for i in range(len(parameters)):
			key = parameters[i]
			info_part = info[i]
			if isinstance(info_part, list):
				info_part = ', '.join(info[i])
			toPrint = "{0}: {1}\n".format(key, info_part)
			print toPrint
		print "\n\n"
