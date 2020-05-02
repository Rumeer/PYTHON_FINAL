#Assign your Genius.com credentials and select your artist
import lyricsgenius as genius
geniusCreds = "{aWD9mHE_T2OGbXwY2kBoVjAJkojVcaYv6VvqwRHpBBcdsd60htyoExWpMdMQ7XFi}"
artist_name = "Jay Electronica"

#Connect your credentials and chosen artist to the genius object then test the first 5 songs
api = genius.Genius(geniusCreds)
artist = api.search_artist(artist_name, max_songs=5)