#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug = True)