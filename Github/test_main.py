#unittest
import unittest
from main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, {greet_person:name}")

if __name__=='__main__':
    unittest.main()

