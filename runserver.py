#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
from ezblog import app

if __name__ == '__main__':
    port = int(os.environ.get("APP_PORT", 5000))
    app.run('127.0.0.1', port=port)