from flask import Flask

app = Flask(__name__)

#when someone visit "/", run the function below
@app.route("/")
def home():
    return "Hello world"

#check if the script is running directly not by importing
if __name__ == "__main__":
    app.run(debug=True)
