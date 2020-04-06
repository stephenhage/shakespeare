import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


#personae = [persona.text for persona in dream.findall('PERSONAE/PERSONA')]
#speakers = set(speaker.text for speaker in dream.findall('*/*/*/SPEAKER'))
#lines = [act.text for act in dream.findall('*/*/*/*/LINE')]

kjv = nltk.Text(gutenberg.words("bible-kjv.txt"))
caesar = nltk.Text(gutenberg.words("shakespeare-caesar.txt"))
macbeth = nltk.Text(gutenberg.words("shakespeare-macbeth.txt"))
hamlet = nltk.Text(gutenberg.words("shakespeare-hamlet.txt"))

print("KJV: {} \nCaeser: {} \nMacbeth: {} \nHamlet: {}".format(len(kjv), len(caesar), len(macbeth), len(hamlet)))