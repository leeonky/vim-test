import unittest
import vim_test as sut


@unittest.skip("Don't forget to test!")
class VimTestTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_test_example()
        self.assertEqual("Happy Hacking", result)
