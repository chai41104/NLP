import affectr
from authorise import Auth

class Theysay :

	def __init__(self):

		authorise = Auth()

		affectr.set_details(authorise.username, authorise.password)

	def getEntity(self, text):

		items = affectr.client.named_entities(text)

		for item in items :
			print(item.head)
			print(item.headIndex)
			print(item.start)
			print(item.end)
			print(item.text)
			print(item.namedEntityTypes)

if __name__ == "__main__":
	theysay = Theysay()
	theysay.getEntity("U.K. Prime Minister Theresa May conceded the response for victims of this week tower block inferno was not good enough, as public criticism of her mounted and police raised the probable death toll to at least 58.")