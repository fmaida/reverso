import reverso
import unittest

class TestReverso(unittest.TestCase):

    def test_is_string(self):
        self.assertTrue(reverso.reverse("Ciao") == "oaiC")
