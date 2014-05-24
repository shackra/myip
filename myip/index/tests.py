from django.test import TestCase, client


class IndexTestCase(TestCase):

    def setUp(self):
        self.c = client.Client()

    def test_index_exists(self):
        """ Existe la pagina principal?
        """
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        response = self.c.get("/")
        self.assertEqual("127.0.0.1" in response.content, True)
