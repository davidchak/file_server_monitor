# coding: utf8

import sys
import time
import sqlite3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



# CONST
PATH = "C:\\Temp"


# TODO: Описать действия при добавлениии/изменении файлов и папок
class Handler(FileSystemEventHandler):
    def __init__(self):
        self.db = 'test.db'

    def sqlite3_con(self, event, isdir, src, dest='None'):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("INSERT INTO events(event, isdir, src, dest) VALUES ('{}','{}','{}','{}')".format(event, isdir, src, dest))
        con.commit()
        con.close()

    def on_created(self, event):
        self.sqlite3_con(event.event_type, event.is_directory, event.src_path)
        print("событие: {}, папка: {}, путь: {}".format(event.event_type, event.is_directory, event.src_path))

    def on_deleted(self, event):
        self.sqlite3_con(event.event_type, event.is_directory, event.src_path)
        print("событие: {}, папка: {}, путь: {}".format(event.event_type, event.is_directory, event.src_path))

    # def on_modified(self, event):
    #     print(event)

    def on_moved(self, event):
        self.sqlite3_con(event.event_type, event.is_directory, event.src_path, event.dest_path)
        print("событие: {}, папка: {}, путь_ист: {}, путь_назн: {}, ".format(event.event_type, event.is_directory, event.src_path, event.dest_path))


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
