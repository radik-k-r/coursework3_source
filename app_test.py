import pytest
from utils import get_posts_all, get_post_by_pk
from app import app
import requests


def test_if_a_list():
    """Возвращается список"""
    all_posts = get_posts_all()
    assert type(all_posts) == list, "it's a list"


def test_code():
    response = requests.get('http://127.0.0.1:5000/api/posts/')
    assert response.status_code == 200


def test_content_by_pk():
    """Проверяет ключи"""
    all_posts = get_posts_all()
    assert all_posts[7]['pk'] == 8, "expected 8"




