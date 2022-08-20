import json


def get_posts_all() -> object:
    """Возвращает список словарей со вложенными постами"""
    with open("data/data.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


def get_comments_all() -> object:
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
                posts.append(post["content"])
            return posts
    except ValueError:
        return "No posts by that user"


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    try:
        post = get_post_by_pk(pk)
        comments = []
        for comment in get_comments_all():
            if comment["post_id"] == post[pk]:
                comments.append(comment["content"])
            return comments
    except ValueError:
        return "No comments by that post"





def get_comments():
    """Возвращает список словарей комментариев"""
    with open("data/comments.json", "r", encoding="utf-8") as file:
        return json.loads(file.read())


def get_post_by_pk(pk):
    """Возвращает пост по номеру"""
    for post in get_posts_all():
        if post['pk'] == pk:
            return post
