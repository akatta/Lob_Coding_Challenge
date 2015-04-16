import api
import json
from angels import *


""" Returns list of top 10 companies based on client """
def get_companies(client, api):
	areas = client.getAreas()
	final_startups = []
	relevant_startups = get_startups_in_area(areas, api)
	final_startups = relevant_startups[:10]
	if len(relevant_startups) > 10:
		relevant_startups = startups_in_industry(client, relevant_startups)
	if len(relevant_startups) > 10:
		relevant_startups = [s for s in relevant_startups if s.getJobs()]
	relevant_startups.sort(key=lambda x : x.get("quality"), reverse=True)
	if relevant_startups:
		final_startups = relevant_startups[:10]
	return final_startups

""" Finds up to 5 pages (250 startups) in each of the areas the client has specified. Maxes out at 5 pages of results to prevent
	the program for running too long. Companies are ordered by popularity on Angel List, however to get the best results first."""
def get_startups_in_area(areas, api):
	area_objects = sum([api.do_get_request("search", {"query":x, "type":"LocationTag"}) for x in areas], [])
	area_ids = [i["id"] for i in area_objects]
	startups = []
	for area in area_ids:
		result = api.do_get_request("tags/{0}/startups".format(area), {"per_page":1})
		last_page = min(5, result["last_page"])
		for i in range(1, last_page + 1):
			search_result = api.do_get_request("tags/{0}/startups".format(area), {"order":"popularity", "page":i})["startups"]
			list_of_startups = [Startup.Startup(x) for x in search_result]
			startups = startups + list_of_startups
	startups = [s for s in startups if not s.hidden()]
	return startups

"""From the startups based in valid areas, finds those related to client's field of interests"""

def startups_in_industry(client, startups):
	interests = client.get("interests")
	startups_in_industry=[s for s in startups if any(x in interests for x in s.getMarkets())]
	return startups_in_industry