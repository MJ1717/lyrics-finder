from flask import Flask, render_template, request
#render template allows to load html files
#and the folder name has to be templates
#request give access to data that user input (so artist name, song title)

app = Flask(__name__)

#when someone visit "/", run the function below
@app.route("/")
def home():
    return render_template("index.html")

#check if the script is running directly not by importing
if __name__ == "__main__":
    app.run(debug=True)
