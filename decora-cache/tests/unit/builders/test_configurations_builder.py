# -*- coding: utf-8 -*-
"""Test Configurations Builder"""


import unittest

from decora-cache.builders.configurations_builder import configurations_builder
from decora-cache.cache.singletons import LocalCacheSingleton
from decora-cache.tests.config import DB, StrictRedis


class TestConfigurationsBuilder(unittest.TestCase):
    def setUp(self):
        self.instance = configurations_builder(DB)

    def test_is_a_callable(self):
        self.assertTrue(callable(configurations_builder))

    def test_return_object(self):
        self.assertIsInstance(self.instance, LocalCacheSingleton)

    def test_has_attr_local_cache(self):
        self.assertIsInstance(self.instance.local_cache, StrictRedis)
