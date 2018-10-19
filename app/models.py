# coding: utf8

from datetime import datetime
from app import db


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(20))
    is_directory = db.Column(db.Boolean)
    src_path = db.Column(db.String(200))
    dst_path = db.Column(db.String(200))
    date = db.Column(db.String(12))
    time = db.Column(db.String(14))

    def __init__(self, event, is_directory, src_path, dst_path):
        self.event = event
        self.is_directory = is_directory
        self.src_path = src_path
        self.dst_path = dst_path
        self.date = self.get_date()
        self.time = self.get_time()

    def __repr__(self):
        return "<Event(event: {}, date: {}, time: {}, is_directory: {} src: {}, dst: {})>".format(
            self.event, self.date, self.time, self.is_directory, self.src_path,
            self.dst_path)

    @staticmethod
    def get_date():
        time = datetime.now()
        return "{}-{}-{}".format(time.day, time.month, time.year)

    @staticmethod
    def get_time():
        time = datetime.now()
        return "{}:{}:{}".format(time.hour, time.minute, time.second)


class File(db.Model):

    def __init__(self, filename, folder):
        self.filename = filename
        self.folder = folder

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), index=True)
    created = db.Column(db.String(10))
    modified = db.Column(db.String(10))
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))


class Folder(db.Model):

    def __init__(self, foldername):
        self.foldername = foldername

    id = db.Column(db.Integer, primary_key=True)
    foldername = db.Column(db.String(256), index=True, unique=True)
    files = db.relationship('File', backref='folder', lazy='dynamic')
    scan_date = db.Column(db.String(20))


class Autor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    autorname = db.Column(db.String(120), index=True, unique=True)
    files = db.relationship('File', backref='autor', lazy='dynamic')
