import sys
import time
import sqlite3
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# from models import Event, session
from app import db
from app.models import Event, File, Folder
from config import PATH_TO_SCAN




# class Handler(FileSystemEventHandler):

#     def on_created(self, event):
#         new_event = Event(event.event_type, event.is_directory, event.src_path, dst_path='')
#         try:
#             db.session.add(new_event)
#             db.session.commit()
#         except Exception as err:
#             print(err)
#         print(new_event)

#     def on_deleted(self, event):
#         new_event = Event(
#             event.event_type, event.is_directory, event.src_path, dst_path='')
#         try:
#             db.session.add(new_event)
#             db.session.commit()
#         except Exception as err:
#             print(err)
#         print(new_event)

#     def on_moved(self, event):
#         new_event = Event(event.event_type, event.is_directory, event.src_path, event.dest_path)
#         try:
#             db.session.add(new_event)
#             db.session.commit()
#         except Exception as err:
#             print(err)
#         print(new_event)


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        '''Обработчик события создания файла или папки и пишет в базу'''
        new_event = Event(event.event_type, event.is_directory, event.src_path, dst_path='')
        db.session.add(new_event)
        db.session.commit()

        if event.is_directory:
            check_folder = Folder.query.filter_by(foldername=event.src_path).first()
            if not hasattr(check_folder, 'foldername'):
                new_folder = Folder(event.src_path)
                db.session.add(new_folder)
                db.session.commit()

        else:
            full_path = re.search(r'(.+)\\(.+)', event.src_path)
            new_folder = Folder(foldername=full_path.group(1))
            check_folder = Folder.query.filter_by(foldername=full_path.group(1)).first()

            if not hasattr(check_folder, 'foldername'):
                db.session.add(new_folder)
                db.session.commit()
            else:
                new_folder = check_folder

            new_file = File(filename=full_path.group(2), folder=new_folder)
            db.session.add(new_file)
            db.session.commit()


    def on_deleted(self, event):
        '''Обработчик события удаления файла или папки'''
        pass


    def on_moved(self, event):
        '''Обработчик события перемещения файла или папки'''
        pass


observer = Observer()
observer.schedule(Handler(), PATH_TO_SCAN, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
