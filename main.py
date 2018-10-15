import sys
import time
import sqlite3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from models import Event, session


PATH = 'C:\\temp'


# TODO: Описать действия при добавлениии/изменении файлов и папок
class Handler(FileSystemEventHandler):

    def on_created(self, event):
        new_event = Event(event.event_type, event.is_directory, event.src_path, dst_path='')
        try:
            session.add(new_event)
            session.commit()
        except Exception as err:
            print(err)
        print(new_event)

    def on_deleted(self, event):
        new_event = Event(
            event.event_type, event.is_directory, event.src_path, dst_path='')
        try:
            session.add(new_event)
            session.commit()
        except Exception as err:
            print(err)
        print(new_event)

    def on_moved(self, event):
        new_event = Event(event.event_type, event.is_directory, event.src_path, event.dest_path)
        try:
            session.add(new_event)
            session.commit()
        except Exception as err:
            print(err)
        print(new_event)


if __name__ == "__main__":
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(Handler(), PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
