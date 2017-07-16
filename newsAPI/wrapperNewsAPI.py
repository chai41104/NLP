from newspaper import Article
import requests
import re


class wrapperNewsAPI(object) :
	def __init__(self) :
		self.listsOfNews = {}
		self.maxNumberOfNews = 1000

	def getText(self, url):
		print(url)
		try:
			article = Article(url)
			article.download()
			html = article.html
			article.parse()
			return [html, article.text]
		except Exception :
			return ["", ""]
		else :
			return ["", ""]	

	def getAllURL(self, inputHTML, patten) :
		urls = re.findall(patten, inputHTML)
		for url in urls :
			# Remove the ending '"'.
			url = url[:-1]
			if url not in self.listsOfNews and len(self.listsOfNews) < self.maxNumberOfNews :
				[html, text] = self.getText(url)
				self.listsOfNews[url] = text
				self.getAllURL(html, patten)

	def getBloombergNews(self, url) :
		# This patten will match all bloomberg-news url ending with '"'.
		BloombergPatten = 'https://www.bloomberg.com/news/articles/[0-9]+[-][0-9]+[-][0-9]+/[[a-zA-Z-]+["]+'
		response = requests.get(url)
		self.getAllURL(response.text, patten)

	def getAllNews(self) :
		return self.listsOfNews

if __name__ == "__main__":
	newsAPI = wrapperNewsAPI()
	urlBloomberg = "https://www.bloomberg.com"
	newsAPI.getBloombergNews(urlBloomberg)