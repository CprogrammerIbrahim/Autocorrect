from Levenshtein import distance
from wordfreq import get_frequency_dict, word_frequency

diction = get_frequency_dict('en')

#Returns a list of Autocorrect proposals for x
def Autocorrect(x):
     neighbourhood = {} #Frequency dict. of words near to x
     for word in diction.keys():
         if distance(x, word) < 3: 
            neighbourhood[word] = word_frequency(word, 'en')
     return sorted(neighbourhood, key=neighbourhood.get, reverse=True)[:3] #First 3 'near' words with highest frequency of use
