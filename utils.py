import json


def get_posts_all() -> object:
    """Возвращает список словарей со вложенными постами"""
    with open("data/data.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


def get_post_by_pk(pk):
    """Возвращает пост по номеру"""
    for post in get_posts_all():
        if post['pk'] == pk:
            return post


def get_comments_all() -> list:
    """Возвращает список словарей со вложенными комментариями"""
    with open("data/comments.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


def get_bookmarks():
    """Возвращает закладки"""
    with open("data/bookmarks.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    try:
        posts = []
        for post in get_posts_all():
            if post["poster_name"] == user_name:
                posts.append(post)
        return posts
    except ValueError:
        return "No posts by that user"


def get_posts_by_text(text):
    """Возвращает посты определенного пользователя"""
    try:
        posts = []
        for post in get_posts_all():
            if text in post['content']:
                posts.append(post)
        return posts
    except ValueError:
        return "No posts by that user"


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    try:
        comments = []
        for comment in get_comments_all():
            if comment['post_id'] == post_id:
                comments.append(comment)
        return comments
    except ValueError:
        return "No comments by that post"





def count_comments():
    """Подсчитывает количество комментариев"""
