import pytest

from core.apps.products.services.products import (
    BaseProductServices,
    ORMProductServices,
)


@pytest.fixture
def product_service() -> 'BaseProductServices':
    return ORMProductServices()