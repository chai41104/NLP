from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features

class Watsonapi(object) :

  def __init__(self):
    # counter
    self.correct = 0
    self.wrong = 0
    self.missing = 0
    self.name = "IBMwantson"

  def getEntity(self, text):

    natural_language_understanding = NaturalLanguageUnderstandingV1(
    username="a6c163eb-4e8a-42ad-a333-f8aec3995bbc",
    password="lVPvtm7YWwAT",
    version="2017-02-27")

    response = natural_language_understanding.analyze(
      text=text,
      features=[
        Features.Entities(
          # Entities options
          sentiment=True
          )
      ]
    )

    output = []

    # Look inside data
    for word in response["entities"] :
      output.append((word['text'], word['type']))
    return output

  def checkClassify(self, ner, correctNer):
    if 'O' in ner and 'O' in correctNer :
      return True
    elif 'Location' in ner and 'geo' in correctNer :
      return True
    elif 'Location' in ner and 'gpe' in correctNer :
      return True
    elif 'Person' in ner and 'per' in correctNer :
      return True
    elif 'Organization' in ner and 'org' in correctNer :
      return True
    elif 'Company' in ner and 'org' in correctNer :
      return True
    elif 'PrintMedia' in ner and 'org' in correctNer :
      return True
    elif 'MISC' in ner and 'gpe' in correctNer :
      return True
    elif 'DATE' in ner and 'tim' in correctNer :
      return True
    if 'O' in correctNer :
      return True
    return False

  def process(self, text, mark) :
    output = self.getEntity(text)
    for (word, ner) in output :
      if word not in mark :
        continue
      correctNer = mark[word]
      if self.checkClassify(ner, correctNer) :
        self.correct += 1
      # elif ner is 'O' :
      #   self.missing += 1
      #   print(word, ' is misclassify ', correctNer)
      else :
        self.wrong += 1
        print(word, ' is classify as ', ner, ' but it should be ', correctNer, ' in ', self.name) 

  def showStatistic(self) :
    print(self.name)
    print('Classify correctly : ', self.correct)
    print('Classify wrong : ', self.wrong)
    print('Misclassify : ', self.missing)
    return (self.correct, self.wrong, self.missing)

if __name__ == "__main__":
  watson = Watsonapi()
  watson.getEntity("U.K. Prime Minister Theresa May conceded the response for victims of this week tower block inferno was not good enough, as public criticism of her mounted and police raised the probable death toll to at least 58.")
