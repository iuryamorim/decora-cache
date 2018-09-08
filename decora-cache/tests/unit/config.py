# -*- coding: utf-8 -*-
"""Test config"""


from redis import StrictRedis


DATABASES = {"default": {"host": "127.0.0.1",
                         "port": 6379,
                         "db": 0,
                         "socket_timeout": 5 / 2.0},
             "test": {"host": "127.0.0.1",
                      "port": 6379,
                      "db": 0,
                      "socket_timeout": 5 / 2.0}}

DB = StrictRedis(**DATABASES['default'])
