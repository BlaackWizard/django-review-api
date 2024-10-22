from core.apps.products.services.products import BaseProductServices, ORMProductServices
import pytest


@pytest.fixture
def product_service() -> 'BaseProductServices':
    return ORMProductServices()