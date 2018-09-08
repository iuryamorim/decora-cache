# -*- encoding: utf-8 -*-
"""Local Cache File"""


from decora-cache.cache.localcache import LocalCache


class CuratedContentLocalCache(LocalCache):
    """Curated content local cache class"""

    def __init__(self, instance):
        """Instance values"""

        self.__key = getattr(instance, 'key', None)
        self.__internal_key = getattr(instance, 'internal_key', None)
        self.expire = getattr(instance, 'cache_expire', 0)
        self.__local_key = None
        self.__builder_values()
        super(CuratedContentLocalCache, self).__init__(self.__local_key, self.expire)

        self.__request_parser = getattr(instance, 'request_parser', None)
        self.__response_parser = getattr(instance, 'response_parser', None)
        self.__response_validation = getattr(instance, 'response_validation', None)

    def __builder_values(self):
        """Build instance values"""

        if self.__internal_key:
            self.__local_key = '{}_{}_curated_local_cache'.format(self.__key, self.__internal_key)
        else:
            self.__local_key = '{}_curated_local_cache'.format(self.__key)

    def get(self):
        """Get local cache"""

        result = self.get_cache()

        if result is not None and self.__response_parser:
            result = CuratedContentLocalCache.execute_parser(self.__response_parser, result)

        if result is not None and self.__response_validation:
            CuratedContentLocalCache.execute_validation(self.__response_validation, result)

        return result

    def set(self, value):
        """Set local cache"""

        if self.__request_parser:
            value = CuratedContentLocalCache.execute_parser(self.__request_parser, value)

        if type(value) not in [str, unicode]:
            raise TypeError(u"Value must be string.")

        return self.set_cache(value)
