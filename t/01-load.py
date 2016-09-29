import unittest
from Spreadsheet.HTML import Table

class TestLoad(unittest.TestCase):

    def test_load(self):
        self.assertTrue( Table() )

if __name__ == '__main__':
    unittest.main()
