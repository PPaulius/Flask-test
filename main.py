from flask import Flask, render_template,  request
import calendar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<word>")
def word(word):
    return render_template("word.html", word = word)

@app.route("/keliamieji")
def leap():
    return render_template("leap.html", calendar = calendar)

@app.route("/arkeliamieji", methods=["GET", "POST"])
def isleap():
    if request.method == "GET":
        return render_template("getyear.html")
    elif request.method == "POST":
        year = request.form["year"]
        return render_template("isleap.html", year=int(year), calendar=calendar)

if __name__ == "__main__":
    app.run(debug=True)