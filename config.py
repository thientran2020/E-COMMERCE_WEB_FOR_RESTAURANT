import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"5\xabP\xd8\xa6\xf1\xb2\x8cIM\x02\x1e(\xe6'\x02\xf9\xb82\xa3\xf9/\xe5q"

    MONGODB_SETTINGS = { 'db': 'restaurant'}
    