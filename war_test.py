import unittest

from war import war

class TestWar(unittest.TestCase):
    """test class of war.py
    """

    def test_war(self):
        """test method for war
        """
        actual = war()
        self.assertEqual('', actual)

if __name__ == "__main__":
    unittest.main()
