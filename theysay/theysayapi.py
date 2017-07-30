import affectr
from authorise import Auth
import os, sys

class Theysay(object) :

	def __init__(self):

		# counter
		self.correct = 0
		self.wrong = 0
		self.missing = 0

		authorise = Auth()
		affectr.set_details(authorise.username, authorise.password)

	def getEntity(self, text):

		items = affectr.client.named_entities(text)

		output = []

		# Look inside data
		for item in items :
			output.append((item.text, item.namedEntityTypes[0]))

		return output

	def checkClassify(self, ner, correctNer):
		if 'ENTITY' in ner and correctNer is 'O' :
			return True
		elif 'LOCATION' in ner and 'geo' in correctNer :
			return True
		elif 'PEOPLE' in ner and 'per' in correctNer :
			return True
		elif 'ORGANISATION' in ner and 'org' in correctNer :
			return True
		elif 'DATE' in ner and 'tim' in correctNer :
			return True
		return False

	def process(self, text, mark) :
		output = self.getEntity(text)
		for (word, ner) in output :
			words = word.split(' ')
			word = words[-1]
			if word not in mark :
				continue
			correctNer = mark[word]
			if self.checkClassify(ner, correctNer) :
				self.correct += 1
			elif ner is 'O' :
				self.missing += 1
				print(word, ' is misclassify ', correctNer)
			else :
				self.wrong += 1
				print(word, ' is classify as ', ner, ' but it should be ', correctNer)

	def showStatistic(self) :
		print('Classify correctly : ', self.correct)
		print('Classify wrong : ', self.wrong)
		print('Misclassify : ', self.missing)
		return (self.correct, self.wrong, self.missing)

if __name__ == "__main__":
	theysay = Theysay()
	theysay.getEntity("U.K. Prime Minister Theresa May conceded the response for victims of this week tower block inferno was not good enough, as public criticism of her mounted and police raised the probable death toll to at least 58.")