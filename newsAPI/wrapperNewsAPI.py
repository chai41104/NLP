from newspaper import Article
import requests
import re


class WrapperNewsAPI(object) :
	def __init__(self) :
		self.listsOfNews = {}
		self.maxNumberOfNews = 1000

	def getText(self, url):
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
				yield ((url, text))
				self.getAllURL(html, patten)

	def getBloombergNews(self, url="https://www.bloomberg.com") :
		# This patten will match all bloomberg-news url ending with '"'.
		BloombergPatten = 'https://www.bloomberg.com/news/articles/[0-9]+[-][0-9]+[-][0-9]+/[[a-zA-Z-]+["]+'
		response = requests.get(url)
		return self.getAllURL(response.text, BloombergPatten)
		

	def getAllNews(self) :
		return self.listsOfNews

if __name__ == "__main__":
	newsAPI = WrapperNewsAPI()
	urlBloomberg = "https://www.bloomberg.com"
	newsGenerater = newsAPI.getBloombergNews(urlBloomberg)
	print(next(newsGenerater))
	print(next(newsGenerater))
	print(next(newsGenerater))