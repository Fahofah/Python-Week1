import unittest

class TestObjectList(unittest.TestCase):
    def test_count(self):
        self.assertCountEqual(len(minWaste_list),3)

if __name__ == '__main__':
    unittest.main()