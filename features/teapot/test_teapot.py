import unittest
from features.teapot.teapot import Teapot

class TestTeapot(unittest.TestCase):

    def test_main(self):
        t=Teapot()
        t.main()
        assert True


    def test_teapot(self):
        t=Teapot()
        t.save()
        assert True

