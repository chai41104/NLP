from loaddata.load import Load
from stanfordCoreNLP.coreclpapi import coreclpapi

class Main(object) :

	def __init__(self):
		self.load = Load()
		self.coreclp = coreclpapi()

	def process(self) :
		inputGenerater = self.load.getData()
		try :
			while True :
				(text, mark) = next(inputGenerater)
				print(text)
				self.coreclp.getEntity(text)
		except StopIteration as e:
			pass
		except Exception as e:
			print(e)

if __name__ == "__main__":
	main = Main()
	main.process()