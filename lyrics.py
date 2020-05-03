import lyricsgenius
import pandas as pd
import string
import nltk
import random
from nltk.corpus import stopwords
from collections import defaultdict

def read_songs(artist_name, song_list):
    """
    returns the list of song lyrics (each songs lyrics is contained within its own item on the list)
    """
    genius = lyricsgenius.Genius("WUThKvy1dkWOTqHFaNxZbt2Sa_QUfvldAmrRZnEXT2p66l24q22V36ISMmss9_JA")
    genius.remove_section_headers = True
    new_list = []
    for x in song_list:
        song = genius.search_song(x, artist_name)
        lyrics=song.lyrics
        new_list.append(lyrics_list(lyrics))
    return new_list

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
def remove_punc(r):
    """
    this function will remove punctuation
    """
    punctuation = string.punctuation
    for p in r:
        if p in punctuation:
            r = r.replace(p,'')
    return r

def markov_chain(new_list):
    """
    Uses new list from read_songs function to generate the markov chain from the list of lyrics
    """
    m_dict=defaultdict(list)
    for x in range(len(new_list)):
        for current_word,next_word in zip(new_list[x][0:-1], new_list[x][1:]):
            m_dict[current_word].append(next_word)
    m_dict = dict(m_dict)
    return m_dict

#print(markov_chain(new_list))

def generate_sentence(m_dict,count=100):
    """
    
    """
    wordl= random.choice(list(m_dict.keys()))
    sentence= wordl.capitalize()
    for i in range(count-1):
        word2=random.choice(m_dict[wordl])
        wordl=word2
        sentence += ' ' + word2
    return(sentence)

# artist_name = "Lupe Fiasco"
# song_list=["Superstar","Deliver","Till I Get There","All Black Everything", "Madonna"]
# song_list=str(song_list)
# print(type(song_list))

# new_list = read_songs(artist_name,song_list)
# print(generate_sentence(markov_chain(new_list)))
