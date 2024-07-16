import pytest
import requests

from main import get_random_cat_image  # Импортируем функцию для тестирования


def test_get_random_cat_image_success(mocker):
    # Мокируем успешный ответ
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'url': 'https://example.com/cat.jpg'}

    # Вызываем функцию для тестирования
    result = get_random_cat_image()

    # Проверяем, что функция вернула ожидаемое значение
    assert result == {'url': 'https://example.com/cat.jpg'}

def test_get_random_cat_image_fail(mocker):
    # Мокируем ошибочный ответ
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500
    # Вызываем функцию для тестирования
    result = get_random_cat_image()
    # Проверяем, что функция вернула None
    assert result is None

