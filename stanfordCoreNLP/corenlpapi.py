import requests
import datetime
import urllib.parse as urllib
import ast

class Corenlpapi(object) :

	def __init__(self):
		# counter
		self.correct = 0
		self.wrong = 0
		self.missing = 0
		self.name = "CoreNLP"

	def getEntity(self, text):

		baseurl = "http://corenlp.run/"

		properties = "?properties="

		# consider only in English
		language = '&pipelineLanguage=en'

		annotators = urllib.quote('{"annotators" : "tokenize,ssplit,ner", "date": "' + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  +'"}', safe='~()*!.\'')

		url = baseurl + properties + annotators + language

		while True :
			# Post data to corenlp (stanford) server.
			response = requests.post(url, data=text)

			if 'CoreNLP request timed out. Your document may be too long.' not in response.text :
				break

		# Convert string to dictionary data
		data = ast.literal_eval(response.text)

		output = []

		# Look inside data
		for sentence in data["sentences"] :
			for word in sentence['tokens'] :
				output.append((word['word'], word['ner']))
		return output

	def checkClassify(self, ner, correctNer):
		if 'O' in ner and 'O' in correctNer :
			return True
		elif 'LOCATION' in ner and 'geo' in correctNer :
			return True
		elif 'PERSON' in ner and 'per' in correctNer :
			return True
		elif 'ORGANIZATION' in ner and 'org' in correctNer :
			return True
		elif 'MISC' in ner and 'gpe' in correctNer :
			return True
		elif 'MISC' in ner and 'org' in correctNer :
			return True
		elif 'LOCATION' in ner and 'gpe' in correctNer :
			return True
		elif 'DATE' in ner and 'tim' in correctNer :
			return True
		if 'O' in correctNer :
			return True
		return False

	def process(self, text, mark) :
		output = self.getEntity(text)
		for (word, ner) in output :
			if word not in mark :
				continue
			correctNer = mark[word]
			if self.checkClassify(ner, correctNer) :
				self.correct += 1
			# elif 'O' in ner :
			# 	self.missing += 1
			# 	print(word, ' is misclassify ', correctNer, ' in ', self.name)
			else :
				self.wrong += 1
				print(word, ' is classify as ', ner, ' but it should be ', correctNer, ' in ', self.name)	

	# def process(self, items) :
	# 	texts = ''
	# 	marks = {}
	# 	while len(items) > 0 :
	# 		(text, mark) = items.pop()
	# 		texts += text
	# 		marks.update(mark)

	# 	output = self.getEntity(texts)
	# 	for (word, ner) in output :
	# 		if word not in marks :
	# 			continue
	# 		correctNer = marks[word]
	# 		if self.checkClassify(ner, correctNer) :
	# 			self.correct += 1
	# 		# elif 'O' in ner :
	# 		# 	self.missing += 1
	# 		# 	print(word, ' is misclassify ', correctNer, ' in ', self.name)
	# 		else :
	# 			self.wrong += 1
	# 			print(word, ' is classify as ', ner, ' but it should be ', correctNer, ' in ', self.name)	

	def showStatistic(self) :
		print(self.name)
		print('Classify correctly : ', self.correct)
		print('Classify wrong : ', self.wrong)
		print('Misclassify : ', self.missing)
		return (self.correct, self.wrong, self.missing)

if __name__ == "__main__":
	coreNLP = Corenlpapi()
	coreNLP.getEntity("U.K. Prime Minister Theresa May conceded the response for victims of this week tower block inferno was not good enough, as public criticism of her mounted and police raised the probable death toll to at least 58.")