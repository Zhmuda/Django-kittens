import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Kitten, Breed


# Фикстуры
@pytest.fixture
def create_user():
    user = User.objects.create_user(username='testuser', password='password')
    return user


@pytest.fixture
def create_breed():
    return Breed.objects.create(name='Siamese')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_kitten(create_user, create_breed):
    return Kitten.objects.create(
        name='Барсик',
        color='Серый',
        age_in_months=6,
        description='Милый котёнок',
        breed=create_breed,
        owner=create_user
    )


# Тесты
@pytest.mark.django_db
def test_create_kitten(api_client, create_user, create_breed):
    # Получение JWT токена
    response = api_client.post('/api/token/', {
        'username': 'testuser',
        'password': 'password'
    })

    assert response.status_code == status.HTTP_200_OK
    token = response.data['access']

    # Использование токена для авторизации
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    response = api_client.post('/api/kittens/', {
        'name': 'Мурзик',
        'color': 'Белый',
        'age_in_months': 3,
        'description': 'Очень милый котёнок',
        'breed': create_breed.id
    })
    assert response.status_code == status.HTTP_201_CREATED

