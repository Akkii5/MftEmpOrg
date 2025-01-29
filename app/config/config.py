import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123456@localhost:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
