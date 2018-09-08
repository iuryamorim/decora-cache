# -*- encoding: utf-8 -*-
"""Build LocalCache Instance"""


from decora-cache.cache.singletons import LocalCacheSingleton


def configurations_builder(instance_local_cache):
    """Singleton localcache instance"""
    return LocalCacheSingleton(instance_local_cache)
