import myserver
import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test_translate(self):
        print myserver.translate("Hello how are you")

    def test_startServer(self):
        myserver.main()

if __name__ == '__main__':
    unittest.main()