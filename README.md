How to run: Run the program main.py with the command:
	python main.py -i <input_file>

The Input file can be one of the two sample files inside of the "sample_clients" folder. (Currently consists of akhil.json, john_doe.json, jason.json)

To find the top 10 companies using the akhil.json folder, merely run "python main.py -i sample_clients/akhil.json" from this directory


General Algorithm:
	Each client has several features, including a list of interests and areas they are willing to work in.
	I first got a list of companies in the areas they wanted to work in. Due to the large amount of data,
	I capped the number of results per area to 250 startups. Then, from this list of startups, I filtered out
	those with non-public information and those that were not in the same fields that the client was interested in.
	Then, I only kept the companies that had current job postings on the Angel List site and finally sorted these
	remaining companies by their "quality" (A metric given by Angel List to rank a company) and picked the best 10 to report.

