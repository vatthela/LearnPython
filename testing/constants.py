import os

BASE_URL = 'http://jsonplaceholder.typicode.com'
SKIP_REAL = os.getenv('SKIP_REAL', False)       # default là không skip
SKIP_TAGS = os.getenv('SKIP_TAGS', '').split()