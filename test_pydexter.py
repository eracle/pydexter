# Copyright 2017 Antonio Ercole De Luca
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import skip

from pydexter import DexterClient

import pprint
import unittest
from local_settings import URL


text = 'Dexter is an American television drama.'
entity = 'United_States'
entity2 = 'Dexter_(TV_series)'
category = 'Sport'
query = 'test query'


def pretty_print(data):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)


class TestPyDexter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._sut = DexterClient(URL)

    def test_get_id(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_id
        print('Executing test: test_get_id')
        out = self._sut.get_id(entity)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(out >= 0)

    def test_annotate(self):
        # python -m unittest test_pydexter.TestPyDexter.test_annotate
        print('Executing test: test_annotate')
        out = self._sut.annotate(text, wikiname=False, min_conf=0.5, max_spots=50)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_nice_annotate(self):
        # python -m unittest test_pydexter.TestPyDexter.test_nice_annotate
        print('Executing test: test_nice_annotate')
        out = self._sut.nice_annotate(text, min_conf=0.5)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_spot(self):
        # python -m unittest test_pydexter.TestPyDexter.test_spot
        print('Executing test: test_spot')
        out = self._sut.spot(text, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_get_spots(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_spots
        print('Executing test: test_get_spots')
        out = self._sut.get_spots(entity, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_get_desc(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_desc
        print('Executing test: test_get_desc')
        out = self._sut.get_desc(entity, title_only=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    @skip('Server doesnt work')
    def test_get_candidates(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_candidates
        print('Executing test: test_get_candidates')
        out = self._sut.get_candidates(query, max_candidates=10)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_relatedness(self):
        # python -m unittest test_pydexter.TestPyDexter.test_relatedness
        print('Executing test: test_relatedness')
        out = self._sut.relatedness(entity, entity2, rel_measure="milnewitten", wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    @skip('Not implemented yet')
    def test_spot_relatedness(self):
        # python -m unittest test_pydexter.TestPyDexter.test_spot_relatedness
        print('Executing test: test_spot_relatedness')
        out = self._sut.spot_relatedness()

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_get_target_entities(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_target_entities
        print('Executing test: test_get_target_entities')
        out = self._sut.get_target_entities(entity, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_get_source_entities(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_source_entities
        print('Executing test: test_get_source_entities')
        out = self._sut.get_source_entities(entity, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        self.assertTrue(len(out) > 0)

    def test_get_entity_categories(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_entity_categories
        print('Executing test: test_get_entity_categories')
        out = self._sut.get_entity_categories(entity2, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        # self.assertTrue(len(out) > 0)

    def test_get_belonging_entities(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_belonging_entities
        print('Executing test: test_get_belonging_entities')
        out = self._sut.get_belonging_entities(category, wikiname=False)

        pretty_print('Output: %s' % out)
        # self.assertTrue(out)

    def test_get_parent_categories(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_parent_categories
        print('Executing test: test_get_parent_categories')
        out = self._sut.get_parent_categories(category, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        # self.assertTrue(len(out) > 0)

    def test_get_child_categories(self):
        # python -m unittest test_pydexter.TestPyDexter.test_get_child_categories
        print('Executing test: test_get_child_categories')
        out = self._sut.get_child_categories(category, wikiname=False)

        pretty_print('Output: %s' % out)
        self.assertIsNotNone(out)
        # self.assertTrue(len(out) > 0)

