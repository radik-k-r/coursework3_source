from flask import Flask, render_template
from utils import get_all, get_bookmarks

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    data = get_all()
    bookmarks = get_bookmarks()
    return render_template("index.html", data=data, bookmarks=bookmarks)


@app.route("/post/<user_name>")
def show_posts(user_name):
    return render_template("post.html", user_name=user_name)


@app.route("/bookmarks")
def show_bookmarks():
    return render_template("bookmarks.html")


if __name__ == "__main__":
    app.run(debug=True)
