import os, sys
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'theysay'))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'newsAPI'))

from loaddata.load import Load
from stanfordCoreNLP.coreclpapi import Coreclpapi
from theysay.theysayapi import Theysay
from watson.watsonapi import Watsonapi
from newsAPI.wrapperNewsAPI import WrapperNewsAPI

class Main(object) :

	def __init__(self):

		self.load = Load()
		self.coreclp = Coreclpapi()
		self.theysay = Theysay()
		self.watson = Watsonapi()
		self.news = WrapperNewsAPI()

	def process(self) :
		inputGenerater = self.load.getData()
		try :
			count = 0
			while True :
				print(count)
				count += 1
				(text, mark) = next(inputGenerater)

				if count < 10634 :
					continue

				# with open('output.txt', 'w') as f:
				# 	f.write(text)

				print(text)

				self.coreclp.process(text, mark)
				self.theysay.process(text, mark)
				self.watson.process(text, mark)
				time.sleep(1)
			self.coreclp.showStatistic()
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

				# with open('output.txt', 'w') as f:
				# 	f.write(text)

				print(text)

				# self.coreclp.process(text, mark)
				# self.theysay.process(text, mark)
				# self.watson.process(text, mark)
				# time.sleep(1)
			self.coreclp.showStatistic()
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