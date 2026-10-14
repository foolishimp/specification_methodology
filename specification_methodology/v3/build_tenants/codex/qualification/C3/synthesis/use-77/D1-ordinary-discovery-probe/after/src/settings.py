import os

# APP_TOKEN is the deprecated name for APP_API_TOKEN; still read as a fallback.
TOKEN = os.environ['APP_API_TOKEN'] if 'APP_API_TOKEN' in os.environ else os.environ['APP_TOKEN']
TOKEN_TTL = int(os.environ.get('APP_TOKEN_TTL', '3600'))
