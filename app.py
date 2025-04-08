from flask import Flask, render_template, request
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

    #this is special, this shows on the web
    return f"You searched for '{title}' by '{artist}'"

#check if the script is running directly not by importing
if __name__ == "__main__":
    app.run(debug=True)
