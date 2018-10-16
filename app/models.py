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
