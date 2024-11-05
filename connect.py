import requests


def get_books():
    response = requests.get('http://127.0.0.1:8000/api/books')
    return response.json()

