import pytest
from django.urls import reverse
from app.models import Business
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_list_businesses():
    # Create a test user
    user = User.objects.create_user(username="testuser", password="testpassword")

    # Create a test business
    Business.objects.create(
        name="Test Business",
        address="123 Main St",
        owner_info="John Doe",
        employee_size=10,
    )

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get(reverse('business-list'))
    assert response.status_code == 200
    assert "Test Business" in str(response.content)

@pytest.mark.django_db
def test_create_business():
    # Create a test user
    user = User.objects.create_user(username="testuser", password="testpassword")

    data = {
        "name": "New Business",
        "address": "456 Elm St",
        "owner_info": "Jane Smith",
        "employee_size": 5,
    }

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post(reverse('business-list'), data, format='json')
    assert response.status_code == 201
    assert Business.objects.filter(name="New Business").exists()

# Add more API test cases for update and delete views as needed
