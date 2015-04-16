import sys, getopt
import json
import os
import api
from company_finder import get_companies
from angels import *

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o")
    except getopt.GetoptError:
        print 'main.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'main.py -i <inputfile>'
            sys.exit()
        elif opt == "-i":
            inputfile = arg


    json_file = open(inputfile)
    client_info = json.load(json_file)
    json_file.close()
    angel_api = api.AngelList()
    client = Person.Person(client_info)

    print "Hello {0} here are the top 10 companies you should apply for\n".format(client.get("name"))


    top_ten_companies = get_companies(client, angel_api)
    for company in top_ten_companies:
    	company.printInfo()


if __name__ == "__main__":
    main(sys.argv[1:])


