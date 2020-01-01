# Autocorrect
An implementation of Autocorrect function with Python 3 (using Levenshtein Metric / Word Frequency List). Many languages are supported. 

This function calculates the distances between the given word and dictionary words. Then it returns a list of Autocorrect proposals consisting of nearest words with highest frequency of use in English language.

```python
from Autocorrect import Autocorrect
Aut = Autocorrect('en')

Aut.propose("solitary")
#['military', 'solitary', 'sanitary']

Aut.propose("love")
#['have', 'one', 'like']

Aut.propose("abcense") #This word is misspelled! 
#['absence', 'license', 'incense']
```
This project depends on the packages: `Levenshtein`, `wordfreq`. Which can be installed as follows:

```
pip install python-Levenshtein wordfreq
```

You can install the project with the following commands:

```
git clone https://github.com/CprogrammerIbrahim/Autocorrect.git
cd Autocorrect
sudo python setup.py install 
```
