# -*- encoding: utf-8 -*-
"""Decorators File"""


import json
import logging

from flask import Response

from decora-cache.cache.endpoint_localcache import EndpointLocalCache
from decora-cache.utils.exceptions import NotACallableException


def local_cache(interface):
    """LocalCache decorator"""

    def get():
        """Get localcache data"""

        if callable(interface):
            instance_interface = interface()
            local_cache_instance = EndpointLocalCache(instance_interface.model)
            local_cache_value = local_cache_instance.get()
            if local_cache_value:
                return local_cache_value
        raise NotACallableException()

    def set(data):
        """Set localcache data"""

        if callable(interface):
            instance_interface = interface()
            local_cache_instance = EndpointLocalCache(instance_interface.model)
            local_cache_instance.set(data)
        raise NotACallableException()

    def args_handler(function):
        """localcache decorator runner"""

        def function_wrapper(*args, **kwargs):
            try:
                result = get()
                if result:
                    return Response(json.dumps(result),
                                    mimetype='application/json')
            except Exception as e:
                logging.error(e)

            func_result = function(*args, **kwargs)

            try:
                set(func_result[0].data)
            except Exception as e:
                logging.error(e)
            return func_result
        return function_wrapper

    return args_handler
