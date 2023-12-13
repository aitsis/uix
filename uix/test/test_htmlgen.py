import unittest
from htmlgen import HTMLGen

class TestHTMLGen(unittest.TestCase):
    def setUp(self):
        self.htmlgen = HTMLGen()

    def test_add_header_item(self):
        self.htmlgen.add_header_item('test', 'test_item')
        self.assertEqual(self.htmlgen.header_items['test'], 'test_item')

    def test_add_script_source(self):
        self.htmlgen.add_script_source('test', 'test_script')
        self.assertEqual(self.htmlgen.script_sources['test'], 'test_script')

if __name__ == '__main__':
    unittest.main()