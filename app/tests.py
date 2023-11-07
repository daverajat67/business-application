from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Business

class BusinessModelTest(TestCase):
    def test_create_business(self):
        business = Business.objects.create(
            name="Sample Business",
            address="123 Main St",
            owner_info="John Doe",
            employee_size=10
        )
        self.assertEqual(business.name, "Sample Business")
        self.assertEqual(business.address, "123 Main St")
        self.assertEqual(business.owner_info, "John Doe")
        self.assertEqual(business.employee_size, 10)


class BusinessViewTest(TestCase):
    def test_list_businesses(self):
        response = self.client.get(reverse('business_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_business(self):
        response = self.client.post(
            reverse('business_list'),
            data={
                "name": "Test Business",
                "address": "456 Elm St",
                "owner_info": "Jane Smith",
                "employee_size": 5
            }
        )
        self.assertEqual(response.status_code, 302)  # Check for a redirect
        # Follow the redirect to verify the created object's details
        new_business = Business.objects.get(name="Test Business")
        self.assertEqual(new_business.name, "Test Business")
        # Add more assertions as needed for other fields


class BusinessAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.business = Business.objects.create(
            name="Test Business",
            address="456 Elm St",
            owner_info="Jane Smith",
            employee_size=5
        )

    def test_list_businesses(self):
        response = self.client.get(reverse('business-list'))
        self.assertEqual(response.status_code, 200)

    def test_create_business(self):
        data = {
            "name": "New Business",
            "address": "789 Oak St",
            "owner_info": "John Smith",
            "employee_size": 8
        }
        response = self.client.post(reverse('business-list'), data, format='json')
        self.assertEqual(response.status_code, 201)


