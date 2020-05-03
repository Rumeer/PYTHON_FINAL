from flask import Flask , render_template, request
import lyrics
from lyrics import read_songs , lyrics_list ,markov_chain ,generate_sentence
app=Flask(__name__)
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)

@app.route("/whythis/")
    return render_template("whythis.html")

@app.route("/lyrics/", methods=["GET", "POST"])
def lyrics():
    if request.method == "POST":
        artist_name = str(request.form["artist_name"])
        song_list = list(str(request.form["song_list"]).split(","))
        new_list = read_songs(artist_name, song_list)
        m_dict= markov_chain(new_list)
        sentence= generate_sentence(m_dict, count=100)
        if sentence:
            return render_template(
                "lyric_output.html", artist_name=artist_name , song_list=song_list , sentence=sentence
                )
        else:
            return render_template("artistsong_form.html", error=True)
    return render_template("artistsong_form.html", error=None)
    
# if __name__=="__main__":
#     app.run(debug= False)