import requests
import datetime
import urllib
import ast

class coreclpapi(object) :

	def getEntity(self, text):

		now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

		baseurl = "http://corenlp.run/"

		properties = "?properties="

		annotators = urllib.quote('{"annotators" : "tokenize,ssplit,ner", "date": "' + now  +'"}', safe='~()*!.\'')

		# consider only in English
		language = '&pipelineLanguage=en'

		url = baseurl + properties + annotators + language

		# Post data to corenlp (stanford) server.
		response = requests.post(url, data=text)

		# Convert string to dictionary data
		data = ast.literal_eval(response.text)

		# Look inside data
		for sentence in data["sentences"] :
			for word in sentence['tokens'] :
				if word['ner'] is not "O" :
					print word

if __name__ == "__main__":
	coreclp = coreclpapi()
	coreclp.getEntity("U.K. Prime Minister Theresa May conceded the response for victims of this week tower block inferno was not good enough, as public criticism of her mounted and police raised the probable death toll to at least 58.")