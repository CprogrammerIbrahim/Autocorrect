from Levenshtein import distance
from wordfreq import get_frequency_dict

class Autocorrect(object):
     def __init__(self, language='en', max_advice=3):
          self.diction = get_frequency_dict(language)
          self.max_advice = max_advice
          
     def propose(self, x):
          neighbourhood = {} #Frequency dict. of words near to x
          for word in self.diction.keys():
               if distance(x, word) < 3: 
                    neighbourhood[word] = self.diction[word]
          return sorted(neighbourhood, key=neighbourhood.get, reverse=True)[:self.max_advice] 
