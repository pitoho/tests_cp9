import pytest
import requests

from src.your_models_module import YourPydanticModel
from faker import Faker

fake = Faker()

api_client_url = 'http://localhost/'


class OpenCartAPITest:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_to_cart(self, product_id, quantity):
        endpoint = f"{self.base_url}/index.php?route=api/cart/add"
        payload = {
            'product_id': product_id,
            'quantity': quantity
        }

        try:
            response = requests.post(endpoint, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None


def test_add_to_cart_with_exception(api_client):
    product_id = fake.random_number()
    quantity = fake.random_number()

    api_client.base_url = 'http://invalid.example.com'

    with pytest.raises(requests.RequestException):
        api_client.add_to_cart(product_id, quantity)


if __name__ == "__main__":
    api_test = OpenCartAPITest(base_url="http://myopencart.example.com")
    product_id = 123
    quantity = 2

    result = api_test.add_to_cart(product_id, quantity)

