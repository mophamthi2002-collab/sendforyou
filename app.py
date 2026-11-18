from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loi-nhan")
def love_letter():
    return render_template("letter.html")

if __name__ == "__main__":
    app.run(debug=True)
