import pytest
from src.your_api_module import YourAPIClient


@pytest.fixture
def api_client(request):
    base_url = request.config.getoption("--baseurl")
    return YourAPIClient(base_url)


def pytest_addoption(parser):
    parser.addoption("--baseurl", action="store", default="http://myopencart.example.com/index.php?route=api/cart/add",
                     help="Base URL for API testing")
