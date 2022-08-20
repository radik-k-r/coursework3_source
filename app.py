import logging
from flask import Flask, render_template, request, jsonify
from utils import get_posts_all, get_bookmarks, get_post_by_pk, get_comments_by_post_id, \
    get_posts_by_user, get_posts_by_text, get_comments_all

logging.basicConfig(filename="logs/api.log", level=logging.INFO)
logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")


app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    """Шаг 1 – реализуйте ленту"""
    logging.info('Главная страница запрошена')
    posts = get_posts_all()
    bookmarks = get_bookmarks()
    comments = get_comments_all()
    return render_template("index.html", posts=posts, bookmarks=bookmarks, comments=comments)


@app.route("/posts/<int:post_id>/")
def show_post(post_id):
    """Шаг 2 – Реализуйте просмотр поста"""
    logging.info('Подробная статья запрошена')
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/")
def search_posts():
    """Шаг 3 – реализуйте поиск"""
    if request.args.get('s'):
        posts = get_posts_by_text(request.args.get('s'))
        return render_template("search.html", posts=posts)
    else:
        posts = get_posts_all()
        return render_template("search.html", posts=posts)


@app.route("/users/<username>/")
def show_posts_by_username(username):
    """Шаг 4 – Реализуйте вывод по пользователю"""
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)


@app.route("/post/<user_name>/")
def show_posts(user_name):
    users_post = get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=users_post)


@app.route("/bookmarks/")
def show_bookmarks():
    return render_template("bookmarks.html")


@app.errorhandler(404)
def page_not_found(e):
    """Шаг 5 – Добавьте обработчики ошибок"""
    title = "404 error"
    # note that we set the 404 status explicitly
    return render_template("404.html", title=title, error=e), 404


@app.route("/nindex/")
def nindex():
    posts = get_posts_all()
    bookmarks = get_bookmarks()
    comments = get_comments_all()
    try:
        return render_template("index.html", posts=tosts, bookmarks=bookmarks, comments=comments)
    except Exception as e:
        return render_template("500.html", error=e), 500


@app.route("/api/posts/")
def get_posts_as_json():
    """Шаг 6 – сделайте 2 API - эндпоинта"""
    all_posts = get_posts_all()
    return jsonify(all_posts), 200


@app.route("/api/posts/<int:post_id>")
def get_posts_by_id_as_json(post_id):
    """Шаг 6 – сделайте 2 API - эндпоинта"""
    post = get_post_by_pk(post_id)
    return jsonify(post=post), 200


if __name__ == "__main__":
    app.run(debug=True)
