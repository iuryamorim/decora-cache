# -*- encoding: utf-8 -*-
"""Local Cache File"""


from decora-cache.cache.singletons import LocalCacheSingleton
from decora-cache.utils.exceptions import (
    RequestException, ParserException, NotACallableException, ValidationException
)
from decora-cache.cache_config import MM


class LocalCache(object):
    """Local cache class"""

    def __init__(self, key, expire=MM):
        """Instance values"""
        self.key = key
        self.expire = expire
        self.local_cache = LocalCacheSingleton().local_cache

    def get_cache(self):
        """Execute get local cache"""
        try:
            return self.local_cache.get(self.key)
        except Exception:
            raise RequestException(u"Could not get local cache for key {}".format(self.key))

    def set_cache(self, value):
        """Execute set local cache"""
        try:
            return self.local_cache.setex(self.key, self.expire, value)
        except Exception:
            raise RequestException(u"Unable to set local cache for key {}".format(self.key))

    @staticmethod
    def execute_parser(parser, data):
        """Execute parser data"""
        if callable(parser):
            try:
                return parser(data)
            except Exception:
                raise ParserException()
        else:
            raise NotACallableException()

    @staticmethod
    def execute_validation(validation, data):
        """Execute validation data"""
        if callable(validation):
            try:
                return validation(data)
            except Exception:
                raise ValidationException()
        else:
            raise NotACallableException()
