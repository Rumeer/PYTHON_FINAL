import lyricsgenius
import pandas as pd
import string
import nltk
import random
from nltk.corpus import stopwords
from collections import defaultdict

genius = lyricsgenius.Genius("WUThKvy1dkWOTqHFaNxZbt2Sa_QUfvldAmrRZnEXT2p66l24q22V36ISMmss9_JA")
artist_name = "Joey Bada$$"
genius.remove_section_headers = True




def remove_punc(r):
    """
    this function will remove punctuation
    """
    punctuation = string.punctuation
    for p in r:
        if p in punctuation:
            r = r.replace(p,'')
    return r
def lyrics_list(lyrics):
    """
    this will break apart the text
    """
    lyric = []
    for r in lyrics.split(): 
        r = remove_punc(r)
        r=r.lower()
        lyric.append(r)    
    return lyric

song_list=["GOOD MORNING AMERIKKKA","FOR MY PEOPLE","TEMPTATION","LAND OF THE FREE","DEVASTED", "AMERIKKKAN IDOL"]
new_list = []
for x in song_list:
    song = genius.search_song(x, artist_name)
    lyrics=song.lyrics
    new_list.append(lyrics_list(lyrics))

def markov_chain(new_list):
    m_dict=defaultdict(list)
    # print (new_list)
    for x in range(len(new_list)):
        for current_word,next_word in zip(new_list[x][0:-1], new_list[x][1:]):
            m_dict[current_word].append(next_word)
    m_dict = dict(m_dict)
    return m_dict

#print(markov_chain(new_list))

def generate_sentence(m_dict,count=100):
    wordl= random.choice(list(m_dict.keys()))
    sentence= wordl.capitalize()
    for i in range(count-1):
        word2=random.choice(m_dict[wordl])
        wordl=word2
        sentence += ' ' + word2
    return(sentence)
r_dict = markov_chain(new_list)
print(generate_sentence(r_dict))