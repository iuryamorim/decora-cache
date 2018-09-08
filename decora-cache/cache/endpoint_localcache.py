# -*- encoding: utf-8 -*-
"""Local Cache File"""


from decora-cache.utils.singletons import LocalCacheSingleton
from decora-cache.utils.exceptions import (
    RequestException, ParserException, NotACallableException, ValidationException
)
from decora-cache.localcache.localcache import LocalCache
from decora-cache.localcache.curated_content_localcache import CuratedContentLocalCache


class EndpointLocalCache(LocalCache):
    """Endpoint local cache class"""

    def __init__(self, instance):
        """Instance values"""

        self.__endpoint = getattr(instance, 'cache_endpoint', None)
        self.__param_values = getattr(instance, 'param_values', [])
        self.__expire = getattr(instance, 'cache_expire', 0)
        self.__local_key = None
        self.__builder_values()
        super(EndpointLocalCache, self).__init__(self.__local_key, self.__expire)

        self.__request_parser = getattr(instance, 'request_parser', None)
        self.__response_parser = getattr(instance, 'response_parser', None)
        self.__response_validation = getattr(instance, 'response_validation', None)

    def __builder_values(self):
        """Build instance values"""

        self.__local_key = '{}_{}_endpoint_local_cache'.format(
            self.__endpoint, '_'.join([str(s) for s in self.__param_values])
        )

    def set(self, value):
        """Set local cache"""

        if self.__request_parser:
            value = CuratedContentLocalCache.execute_parser(self.__request_parser, value)

        if type(value) not in [str, unicode]:
            raise TypeError(u"O valor deve ser uma string.")

        if type(value) is dict:
            value['local_cache'] = True

        return self.set_cache(value)

    def get(self):
        """Get local cache"""

        result = self.get_cache()

        if result is not None and self.__response_parser:
            result = EndpointLocalCache.execute_parser(self.__response_parser, result)

        if result is not None and self.__response_validation:
            EndpointLocalCache.execute_validation(self.__response_validation, result)

        return result
