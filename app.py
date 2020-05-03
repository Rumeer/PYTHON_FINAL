from flask import Flask , render_template, request
import lyrics

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)



@app.route("/lyrics/", methods=["GET", "POST"])
def nearest():
    if request.method == "POST":
        place_name = str(request.form["place_name"])
        mbta_stop = find_stop_near(place_name)
        """"
        artist_name = "Lupe Fiasco"
        song_list=["Superstar","Deliver","Till I Get There","All Black Everything", "Madonna"]
        new_list = read_songs(artist_name,song_list)
        print(generate_sentence(markov_chain(new_list)))
        """"
        if mbta_stop:
            return render_template(
                "mbta_result.html", place_name=place_name , mbta_stop=mbta_stop
            )
        else:
            return render_template("mbta_form.html", error=True)
    return render_template("mbta_form.html", error=None)
    
if __name__=="__main__":
    app.run(debug=True)