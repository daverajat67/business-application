# tests/test_models.py
from app.models import Business
import pytest

@pytest.mark.django_db
def test_create_business():
    business = Business.objects.create(
        name="Sample Business",
        address="123 Main St",
        owner_info="John Doe",
        employee_size=10
    )
    assert business.name == "Sample Business"
    assert business.address == "123 Main St"
    assert business.owner_info == "John Doe"
    assert business.employee_size == 10
