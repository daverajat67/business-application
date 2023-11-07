import pytest
from django.urls import reverse
from app.models import Business
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_list_businesses(client):
    # Create a test user and log in
    user = User.objects.create_user(username="testuser", password="testpassword")
    client.login(username="testuser", password="testpassword")

    # Create a test business
    Business.objects.create(
        name="Test Business",
        address="123 Main St",
        owner_info="John Doe",
        employee_size=10,
    )

    response = client.get(reverse('business_list'))
    assert response.status_code == 200
    assert "Test Business" in str(response.content)

@pytest.mark.django_db
def test_create_business(client):
    # Create a test user and log in
    user = User.objects.create_user(username="testuser", password="testpassword")
    client.login(username="testuser", password="testpassword")

    data = {
        "name": "New Business",
        "address": "456 Elm St",
        "owner_info": "Jane Smith",
        "employee_size": 5,
    }

    response = client.post(reverse('business_list'), data)
    assert response.status_code == 302  # Check for a redirect
    assert Business.objects.filter(name="New Business").exists()

# Add more view test cases for update and delete views as needed
