import lyricsgenius
import pandas as pd
genius = lyricsgenius.Genius("_DXQ_ikkLyYiZENSnzV7tfbjG2_s_2wENNFY1njNCd5zNQzXDOC5oW5Dg7IxYOit")
artist_name = "Jay Electronica"
artist = genius.search_artist(artist_name, max_songs=3, sort="popularity")
print(artist.songs)

song = genius.search_song("The Neverending Story", artist.name)
print(song.lyrics)
artist.add_song(song)
artist.save_lyrics()

Artist=pd.read_json("Lyrics_{artist_name}.json")

