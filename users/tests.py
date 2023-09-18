from django.test import SimpleTestCase

# Create your tests here.
class SimpleTest1(SimpleTestCase):
    def test_edf_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)


class SimpleTest2(SimpleTestCase):
    def test_edf_sign(self):
        response = self.client.get('/sign')
        self.assertEqual(response.status_code, 200)


class SimpleTest3(SimpleTestCase):
    def test_edf_sign(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 200)


