import json
import os

class Load(object) :

	def __init__(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.inputfile = dir_path + "/data.json"

	def filterout(self, word) :
		word = word.replace('-', '')
		word = word.replace('"', '')
		word = word.replace('\'', '')
		word = word.replace('…', '.')
		word = word.replace('(', ',')
		word = word.replace(')', ',')
		word = word.replace('~', ' ')
		word = word.replace('’', '')
		word = word.replace('–', ',')
		word = word.replace('”', '')
		return word

	def preprocess(self, word) :
		if word.startswith('.') :
			return word
		else :
			return ' ' + word
		
	def getData(self) :
		with open(self.inputfile, 'r') as json_data:
			json_list = json.loads(list(json_data)[0])
			for sentences in json_list :
				if len(json_list) < 10 :
					continue 
				raw_data = ""
				mark = {}
				for word in sentences :
					newWord = self.filterout(word[0][0])
					raw_data += self.preprocess(newWord)
					mark[newWord] = word[1]
				yield (raw_data, mark)

if __name__ == "__main__":
	load = Load()
	inputGenerater = load.getData()
	print(next(inputGenerater))
	print(next(inputGenerater))
	print(next(inputGenerater))
	