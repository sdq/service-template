import os

class Config:
    DEBUG = True
    UPLOADS_DEFAULT_DEST = os.getcwd()
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/'
