# coding: utf8
import os
from app import db
from app.models import File, Folder
from config import PATH_TO_SCAN


def first_scan(dir):
    ''' Выполняет первичное заполение базы данными с файловой системы '''

    tree = os.walk(dir)

    for p, d, f in tree:

        new_folder = Folder(foldername=p)
        db.session.add(new_folder)
        db.session.commit()

        for i in f:

            new_file = File(filename=i, folder=new_folder)
            db.session.add(new_file)
            db.session.commit()


if __name__ == '__main__':
    print('Начато сканирование...')
    first_scan(PATH_TO_SCAN)
    print('Операция завершена')
