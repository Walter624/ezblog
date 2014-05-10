#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
from ezblog import app

if __name__ == '__main__':
    app.run('127.0.0.1', port=app.config['PORT'])