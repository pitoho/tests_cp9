import requests


class YourAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_to_cart(self, product_id, quantity):
        endpoint = f"{self.base_url}&product_id={product_id}&quantity={quantity}"
        response = requests.post(endpoint)
        return response
