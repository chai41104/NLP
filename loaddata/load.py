import json
import os

class Load(object) :

	def __init__(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.inputfile = dir_path + "/data.json"

	def preprocess(self, word) :
		word = word.replace('-', '')
		if word.startswith('.') :
			return word
		elif word.startswith('\'') :
			return word.replace('\'', ' ')
		else :
			return ' ' + word
		
	def getData(self) :
		with open(self.inputfile, 'r') as json_data:
			json_list = json.loads(list(json_data)[0])
			for sentences in json_list :
				raw_data = ""
				mark = {}
				for word in sentences :
					raw_data += self.preprocess(word[0][0])
					mark[word[0][0]] = word[1]
				yield (raw_data, mark)

if __name__ == "__main__":
	load = Load()
	inputGenerater = load.getData()
	print(next(inputGenerater))
	print(next(inputGenerater))
	print(next(inputGenerater))
	