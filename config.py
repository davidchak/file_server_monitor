# coding: utf8

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class DevConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')