# -*- coding: utf-8 -*-
"""Test Curated Content Local Cache"""


import unittest

from decora-cache.models.configuration import ConfigurationModel
from decora-cache.cache.curated_content_localcache import CuratedContentLocalCache
from decora-cache.builders.configurations_builder import configurations_builder
from decora-cache.tests.config import DB


class TestCuratedContentLocalCache(unittest.TestCase):
    def setUp(self):
        configurations_builder(DB)
        configuration = ConfigurationModel()
        self.local_cache = CuratedContentLocalCache(configuration)

    def test_object_instance(self):
        self.assertIsInstance(CuratedContentLocalCache, object)

    def test_has_func_get(self):
        self.assertTrue(callable(self.local_cache.get))

    def test_has_func_set(self):
        self.assertTrue(callable(self.local_cache.set))

    def test_set(self):
        self.assertTrue(self.local_cache.set('{ "test": "test" }'))

    def test_get(self):
        self.local_cache.set('{ "test": "test" }')
        self.assertEqual(self.local_cache.get(), {'test': 'test'})
