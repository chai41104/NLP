import requests
import datetime
import urllib.parse as urllib
import ast

class Coreclpapi(object) :

	def __init__(self):
		# counter
		self.correct = 0
		self.wrong = 0
		self.missing = 0

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

		output = []

		# Look inside data
		for sentence in data["sentences"] :
			for word in sentence['tokens'] :
				output.append((word['word'], word['ner']))

		return output

	def checkClassify(self, ner, correctNer):
		if ner is 'O' and correctNer is 'O' :
			return True
		elif 'LOCATION' in ner and 'geo' in correctNer :
			return True
		elif 'PERSON' in ner and 'per' in correctNer :
			return True
		elif 'ORGANIZATION' in ner and 'org' in correctNer :
			return True
		elif 'MISC' in ner and 'gpe' in correctNer :
			return True
		elif 'DATE' in ner and 'tim' in correctNer :
			return True
		return False

	def process(self, text, mark) :
		output = self.getEntity(text)
		for (word, ner) in output :
			correctNer = mark[word]

			if self.checkClassify(ner, correctNer) :
				self.correct += 1
			elif ner is 'O' :
				self.missing += 1
				# print(word, ' is misclassify ', correctNer)
			else :
				self.wrong += 1
				# print(word, ' is classify as ', ner, ' but it should be ', correctNer)	

	def showStatistic(self) :
		print('Classify correctly : ', self.correct)
		print('Classify wrong : ', self.wrong)
		print('Misclassify : ', self.missing)
		return (self.correct, self.wrong, self.missing)

if __name__ == "__main__":
	coreclp = Coreclpapi()
	coreclp.getEntity("U.K. Prime Minister Theresa May conceded the response for victims of this week tower block inferno was not good enough, as public criticism of her mounted and police raised the probable death toll to at least 58.")