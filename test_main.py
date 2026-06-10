# Модель: Математичне моделювання біологічного росту бактерій (5 семестр)
# Автор: Бордіян Микола Павлович, група AI-231

import unittest
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/calculate')
        self.assertNotEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
