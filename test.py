import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(main.main("C:\\Users\\HP\\Desktop\\BookCovers"), ' VECTOR MECHANICS FOR ENGINEERS and Dynamics')

if __name__ == '__main__':
    unittest.main()