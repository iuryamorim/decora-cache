# -*- encoding: utf-8 -*-
"""Singletons File"""


class LocalCacheSingleton(object):
    """Local cache singleton class"""

    def __new__(cls, instance_local_cache=None):
        """Create instance local cache singleton"""

        if not hasattr(cls, 'instance'):
            cls.instance = super(LocalCacheSingleton, cls).__new__(cls)
            cls.local_cache = instance_local_cache
        return cls.instance
