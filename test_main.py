# Модель: Математичне моделювання біологічного росту бактерій (5 семестр)
# Автор: Бордіян Микола Павлович, група AI-231

import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_route(client):
    # Тест перевіряє, чи повертає API відповідь 200 або 400 (залежно від логіки)
    # для запиту без даних
    response = client.post('/calculate', json={})
    assert response.status_code == 200
