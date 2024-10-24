import pytest
from tests.factories.products import ProductModelFactory

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilter
from core.apps.products.services.products import BaseProductServices


@pytest.mark.django_db
def test_products_count_zero(product_service: BaseProductServices):
    """"
    Test product count zero with no products in database
    """
    products_count = product_service.get_product_count(ProductFilter())

    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_products_count_exist(product_service: BaseProductServices):
    """
    Test product count exist with products in database
    """
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    products_count = product_service.get_product_count(ProductFilter())

    assert products_count == expected_count

@pytest.mark.django_db
def test_get_zero_products(product_service: BaseProductServices):
    """
    Test get products without products
    """
    product_list = product_service.get_product_list(ProductFilter(), PaginationIn())

    assert product_list == [], f"{product_list=}"

@pytest.mark.django_db
def test_get_product_list(product_service: BaseProductServices):
    """
    Test get product list with products in database
    """
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    product_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilter(), PaginationIn())
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_titles) == expected_count, f'{fetched_titles=}'
    assert product_titles == fetched_titles, f'{product_titles=}'


