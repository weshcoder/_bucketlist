from flask_testing import TestCase
from app import create_app

class TestCase(TestCase):
    def create_app(self):
        """
        Instantiate app instance
        """
        app = create_app(config_name="testing")
        return app

    def test_home(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()