import unittest
from main import add

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
<<<<<<< HEAD
    unittest.main()
=======
    unittest.main()
>>>>>>> 346e305 (Add GitHub Actions workflow)
