# -*- coding: utf-8 -*-
"""Test Endpoint Local Cache"""


import unittest

from decora-cache.models.configuration import ConfigurationModel
from decora-cache.utils.localcache import EndpointLocalCache
from decora-cache.utils.configurations_builder import configurations_builder
from decora-cache.tests.config import Redis, DB


class TestEndpointLocalCache(unittest.TestCase):
    def setUp(self):
        configurations_builder(DB)
        configuration = ConfigurationModel()
        self.local_cache = EndpointLocalCache(configuration)

    def test_object_instance(self):
        self.assertIsInstance(EndpointLocalCache, object)

    def test_has_func_get(self):
        self.assertTrue(callable(self.local_cache.get))

    def test_has_func_set(self):
        self.assertTrue(callable(self.local_cache.set))

    def test_set(self):
        self.assertTrue(self.local_cache.set('{ "test": "test" }'))

    def test_get(self):
        self.local_cache.set('{ "test": "test" }')
        self.assertEqual(self.local_cache.get(), {'test': 'test'})
