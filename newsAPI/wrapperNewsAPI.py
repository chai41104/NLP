from newspaper import Article

class wrapperNewsAPI(object) :
	def getText(self, url):
		article = Article(url)
		article.download()
		article.parse()
		print(article.text)
		return article.text
	

if __name__ == "__main__":
	url = 'https://www.bloomberg.com/news/articles/2017-07-14/blair-says-u-k-should-keep-open-the-option-of-staying-in-eu'
	newsAPI = wrapperNewsAPI()
	newsAPI.getText(url)