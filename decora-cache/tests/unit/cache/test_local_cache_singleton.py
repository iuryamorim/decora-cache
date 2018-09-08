# -*- coding: utf-8 -*-
"""Test Local Cache Singleton"""


import unittest

from decora-cache.cache.singletons import LocalCacheSingleton
from decora-cache.builders.configurations_builder import configurations_builder
from decora-cache.tests.config import DB, StrictRedis


class TestLocalCacheSingleton(unittest.TestCase):
    def setUp(self):
        configurations_builder(DB)
        self.instance = LocalCacheSingleton(DB)

    def test_is_a_callable(self):
        self.assertTrue(callable(LocalCacheSingleton))

    def test_return_object(self):
        self.assertIsInstance(self.instance, LocalCacheSingleton)

    def test_instance_is_singleton(self):
        self.assertIs(self.instance, LocalCacheSingleton(DB))

    def test_has_attr_local_cache(self):
        self.assertIsInstance(self.instance.local_cache, StrictRedis)
