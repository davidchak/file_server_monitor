# coding: utf8

from flask import render_template
from app import app, db


@app.route('/')
def index_page():
    return '<h3>TEST ПРОВЕРКА TEST<h3>'
