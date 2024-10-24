import random
from abc import (
    ABC,
    abstractmethod,
)
from django.core.cache import cache

from core.apps.customers.entities import CustomerEntity


class BaseCodeServices(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str:
        ...

    @abstractmethod
    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        ...

class DjangoCacheCodeServices(BaseCodeServices):

    def generate_code(self, customer: CustomerEntity) -> str:
        code = str(random.randint(100000, 9999999))
        cache.set(customer.phone, code)
        return code

    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        code = cache.get(customer.phone)
        