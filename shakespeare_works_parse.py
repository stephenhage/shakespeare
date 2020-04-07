import nltk
from nltk.corpus import gutenberg, shakespeare
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import xml.etree.ElementTree as ET

plays_list_url = "http://shakespeare.mit.edu/"
plays_dict = dict()
def get_links_to_works(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    plays_list = soup.findAll("table")[1]
    for elem in plays_list.findAll('a'):
        plays_dict[elem.text.replace("\n", "")] = plays_list_url + elem['href'].replace("index", "full")
get_links_to_works(plays_list_url)
print(plays_dict)
play_text_dict = dict()
def get_play_text(play, url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    play_text_dict[play] = soup

for key, value in plays_dict.items():
    print(key, value)
    get_play_text(key, value)

# pd.DataFrame(play_text_dict).to_csv("plays_text.csv")
# print(play_text_dict)


# get_play_text("http://shakespeare.mit.edu/allswell/index.html")
# print(list(plays_dict.values())[0])
# print(plays_dict.items[1])
# for play, url in plays_dict.items():
#     print(url)
# print(plays_list.findAll('td'))
# for cell in plays_list:
#     print(cell.find_all('href'))
    # for play in link.find('td'):
    #     print(play.href)


# print(soup.findAll('table'))
#
# dream = shakespeare.xml("dream.xml")
# personae = [persona.text for persona in dream.findall('PERSONAE/PERSONA')]
# speakers = set(speaker.text for speaker in dream.findall('*/*/*/SPEAKER'))
# speaker_order = [speaker.text for speaker in dream.findall('*/*/*/SPEAKER')]
#
# #lines = [act.text for act in dream.findall('*/*/*/*/LINE')]
#
# kjv = nltk.Text(gutenberg.words("bible-kjv.txt"))
# caesar = nltk.Text(gutenberg.words("shakespeare-caesar.txt"))
# macbeth = nltk.Text(gutenberg.words("shakespeare-macbeth.txt"))
# hamlet = nltk.Text(gutenberg.words("shakespeare-hamlet.txt"))
#
# print("KJV: {} \nCaeser: {} \nMacbeth: {} \nHamlet: {}".format(len(kjv), len(caesar), len(macbeth), len(hamlet)))
#
# dream_tree = ET.parse(dream)
# dream_root = dream_tree.getroot()
#
# print(dream_tree, "\n", dream_root)
# #def get_speakers(play):
 #   for