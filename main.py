import os, sys
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'theysay'))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'newsAPI'))

from loaddata.load import Load
from stanfordCoreNLP.corenlpapi import Corenlpapi
from theysay.theysayapi import Theysay
from watson.watsonapi import Watsonapi
from newsAPI.wrapperNewsAPI import WrapperNewsAPI

class Main(object) :

	def __init__(self):

		self.load = Load()
		self.corenlp = Corenlpapi()
		self.theysay = Theysay()
		self.watson = Watsonapi()
		self.news = WrapperNewsAPI()

	def process(self) :
		inputGenerater = self.load.getData()
		try :
			count = 0
			while True :
				count += 1
				print(count)

				(text, mark) = next(inputGenerater)
				self.theysay.process(text, mark)
				self.corenlp.process(text, mark)
				self.watson.process(text, mark)

				time.sleep(1)

			self.corenlp.showStatistic()
			self.theysay.showStatistic()
			self.watson.showStatistic()
		
		except StopIteration as e:
			pass
		except Exception as e:
			print(e)

	def processNews(self) :
		inputGenerater = self.news.getBloombergNews()
		try :
			count = 0
			while True :
				print(count)
				count += 1
				(url, text) = next(inputGenerater)

			self.corenlp.showStatistic()
			self.theysay.showStatistic()
			self.watson.showStatistic()
		
		except StopIteration as e:
			pass
		except Exception as e:
			print(e)


if __name__ == "__main__":
	main = Main()
	main.process()
	# main.processNews()