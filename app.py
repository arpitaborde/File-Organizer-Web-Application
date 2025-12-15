from flask import Flask, render_template, request
from organizer import organize_files

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        directory = request.form["directory"]
        message = organize_files(directory)
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
