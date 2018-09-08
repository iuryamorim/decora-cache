# -*- coding: utf-8 -*-
"""Test Local Cache"""


import unittest
import json

from decora-cache.cache.localcache import LocalCache
from decora-cache.builders.configurations_builder import configurations_builder
from decora-cache.tests.config import StrictRedis, DB


class TestLocalCache(unittest.TestCase):
    def setUp(self):
        configurations_builder(DB)
        self.local_cache = LocalCache('test', 60)

    def test_object_instance(self):
        self.assertIsInstance(LocalCache, object)

    def test_has_attr_key(self):
        self.assertEqual(type(self.local_cache.key), str)

    def test_has_attr_expire(self):
        self.assertEqual(type(self.local_cache.expire), int)

    def test_has_attr_local_cache(self):
        self.assertIsInstance(self.local_cache.local_cache, StrictRedis)

    def test_has_func_execute_parser(self):
        self.assertTrue(callable(self.local_cache.execute_parser))

    def test_has_func_execute_validation(self):
        self.assertTrue(callable(self.local_cache.execute_validation))

    def test_set_cache(self):
        self.assertTrue(self.local_cache.set_cache('test'))

    def test_get_cache(self):
        self.local_cache.set_cache('test')
        self.assertEqual(self.local_cache.get_cache(), 'test')

    def test_execute_parser(self):
        def response_parser(data):
            if type(data) in [str, unicode]:
                return json.loads(data)
            return data

        value = self.local_cache.execute_parser(response_parser, '{}')
        self.assertEqual(value, {})

    def test_execute_validation(self):
        def response_validation(data):
            if type(data) is not dict:
                raise TypeError(u"Configuration should be a dictionary.")
            return data

        value = self.local_cache.execute_validation(response_validation, {})
        self.assertEqual(value, {})
