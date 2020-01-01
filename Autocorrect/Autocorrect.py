from Levenshtein import distance
from wordfreq import get_frequency_dict

class Autocorrect(object):
     def __init__(self, language='en'):
          self.diction = get_frequency_dict(language)
          
     def propose(self, x):
          neighbourhood = {} #Frequency dict. of words near to x
          for word in self.diction.keys():
               if distance(x, word) < 3: 
                    neighbourhood[word] = self.diction[word]
          return sorted(neighbourhood, key=neighbourhood.get, reverse=True)[:3] 
