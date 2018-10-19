# coding: utf8

from flask import jsonify
from app import app, db


@app.route('/')
def index_page():
    data = {
        'autor': 'Давид Чакирян',
        'name': 'Сканер файлов',
        'version': '0.0.1'
    }

    return jsonify(data)


@app.route('/search/<query_str>')
def search_engine(query_str):
    data = File.query.filter(File.filename.contains(query_str).all())
    return data