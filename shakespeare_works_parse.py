import requests
from bs4 import BeautifulSoup as bs
import os
import pandas as pd
import sqlite3
import urllib.request

plays_list_url = "http://shakespeare.mit.edu/"
plays_dict = dict()
def get_links_to_works(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    plays_list = soup.findAll("table")[1]
    for elem in plays_list.findAll('a'):
        plays_dict[elem.text.replace("\n", "")] = plays_list_url + elem['href'].replace("index", "full")
get_links_to_works(plays_list_url)

play_text_dict = dict()
def get_play_text(play, url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    play_text_dict[play] = soup

for key, value in plays_dict.items():
    get_play_text(key, value)

test_url = "http://shakespeare.mit.edu/allswell/full.html"
plays_text = dict()

def write_to_local(play):
    with open(play + '.html', 'wb') as file:
        file.write(play_text_dict[play].prettify('utf-8'))

for play in plays_dict.keys():
    if not os.path.exists(play + '.html'):
        write_to_local(play)

def scrape_text(play):
    play_html = bs(open(play), "html.parser")
    play_text = list()
    play_speechname = list()
    for line in play_html.find_all('a', {"name": True}):
        if line and len(line) >0:
            line_text = line.text.strip().replace("\n", "")
            play_text.append(line_text)
            play_speechname.append(line['name'])
    playname = play_html.find('table').find('td').text.replace("\n", "").strip().split('  ')[0]
    return pd.DataFrame({'texttype': play_speechname,
                          'text': play_text,
                       'play': [playname] * len(play_speechname)})

def clean_play_dat(df):
    df['joincol'] = df.index
    df_speakers = df.loc[df.texttype.str.contains("speech"), ["text", "joincol", 'texttype']]
    df_speakers.columns = ['speaker', 'joincol', 'speechno']
    df_speeches = df.loc[~df.texttype.str.contains("speech"), ["texttype", "text", "joincol", "play"]]
    clean_df = pd.merge_asof(df_speeches, df_speakers, on = 'joincol', direction = 'backward')
    clean_df[['act', 'scene', 'line']] = clean_df.texttype.str.split(".", expand = True)
    return clean_df

listofplays = list()

for file in os.listdir():
    if file.endswith(".html"):
        listofplays.append(file)

list_of_poems = ["The Sonnets.html",
"A Lover's Complaint.html",
"The Rape of Lucrece.html",
"Venus and Adonis.html",
"Funeral Elegy by W.S..html"]
listofplays = [play for play in listofplays if play not in list_of_poems]

con = sqlite3.connect("data/shakespeare.sqlite")
cur = con.cursor()

for play in listofplays:
    df = scrape_text(play)
    clean_df = clean_play_dat(df)
    clean_df[["play", "text", "speaker", "speechno", "act", "scene", "line"]].to_sql("speakers", con, if_exists = "append", index = False)