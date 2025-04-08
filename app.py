from flask import Flask, render_template, request
import requests
#render template allows to load html files
#and the folder name has to be templates
#request give access to data that user input (so artist name, song title)


app = Flask(__name__)



#when someone visit "/", run the function below
@app.route("/")
def home():
    return render_template("index.html")



#post is sending, user sending data to the server
@app.route("/lyrics", methods=["POST"])
def get_lyrics():
    # Get form input values
    artist = request.form["artist"]
    title = request.form["title"]

    #make api url with artist and title
    api_url = f"https://api.lyrics.ovh/v1/{artist}/{title}"

    response = requests.get(api_url, headers={"User-Agent": "Mozilla/5.0"})

    #convert it to json, (to dic), much easiwer to read
    data = response.json()
    #data have one key named 'lyrics' if there exist song that matches

    if 'lyrics' in data:
        lyrics = data['lyrics']
    else:
        lyrics = "No lyrics found with given data" 

    return lyrics

    



#check if the script is running directly not by importing
if __name__ == "__main__":
    app.run(debug=True)
