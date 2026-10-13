import os

TOKEN = os.environ['APP_TOKEN']
TOKEN_TTL = int(os.environ.get('APP_TOKEN_TTL', '3600'))
