import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://root:root@localhost:5432/voicebot"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
