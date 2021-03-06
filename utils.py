import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

from rq import Queue
from workers import conn

q = Queue(connection=conn)

from utils import count_words_at_url

result = q.enqueue(count_words_at_url, 'http://heroku.com')