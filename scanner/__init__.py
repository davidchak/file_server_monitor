import sys
import time
import sqlite3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# from models import Event, session
from app import db
from app.models import Event


PATH_TO_SCAN = 'C:\\temp'


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        new_event = Event(event.event_type, event.is_directory, event.src_path, dst_path='')
        try:
            db.session.add(new_event)
            db.session.commit()
        except Exception as err:
            print(err)
        print(new_event)

    def on_deleted(self, event):
        new_event = Event(
            event.event_type, event.is_directory, event.src_path, dst_path='')
        try:
            db.session.add(new_event)
            db.session.commit()
        except Exception as err:
            print(err)
        print(new_event)

    def on_moved(self, event):
        new_event = Event(event.event_type, event.is_directory, event.src_path, event.dest_path)
        try:
            db.session.add(new_event)
            db.session.commit()
        except Exception as err:
            print(err)
        print(new_event)


observer = Observer()
observer.schedule(Handler(), PATH_TO_SCAN, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()