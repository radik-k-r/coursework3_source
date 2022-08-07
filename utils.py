import json


def get_all():
    """Возвращает посты"""
    with open("data/data.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())

def get_comments_from_json():
    pass


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    try:
        posts = []
        for post in get_all():
            if post["poster_name"] == user_name:
                posts.append(post["content"])
            return posts
    except ValueError:
        return "No posts by that user"


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    try:
        comments = []
        for comment in get_all():
            if comment["poster_name"] == post_id:
                comments.append(comment["content"])
            return comments
    except ValueError:
        return "No comments by that post"


def get_bookmarks():
    """Возвращает закладки"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())