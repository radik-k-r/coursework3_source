from flask import Flask, render_template, request
from utils import get_posts_all, get_bookmarks, get_post_by_pk, get_comments, get_comments_by_post_id, \
    get_posts_by_user, get_posts_by_text

app = Flask(__name__)


@app.route("/")
def homepage():
    posts = get_posts_all()
    bookmarks = get_bookmarks()
    return render_template("index.html", posts=posts, bookmarks=bookmarks)


@app.route("/post/<user_name>")
def show_posts(user_name):
    users_post = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=users_post)


@app.route("/bookmarks")
def show_bookmarks():
    return render_template("bookmarks.html")


@app.route("/user-feed")
def show_feeds():
    return render_template("user-feed.html")


@app.route("/posts/<int:pk>")
def show_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search")
def search_posts():
    if request.args.get('s'):
        posts = get_posts_by_text(request.args.get('s'))
        return render_template("search.html", posts=posts)
    else:
        posts = []
    return render_template("search.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
