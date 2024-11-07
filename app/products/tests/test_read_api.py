from django.test import SimpleTestCase

class TestReadAPI(SimpleTestCase):
    def test_filter(self):
        a = 10
        self.assertEqual(a, 50)