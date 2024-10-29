from abc import (
    ABC,
    abstractmethod,
)
from uuid import uuid4

from core.apps.customers.entities import CustomerEntity
from core.apps.customers.models import Customer


class BaseCustomerServices(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> CustomerEntity:
        ...

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str:
        ...

    @abstractmethod
    def get(self, phone: str) -> CustomerEntity:
        ...


class ORMCustomerServices(BaseCustomerServices):

    def get_or_create(self, phone: str) -> CustomerEntity:
        customer_dto, _ = Customer.objects.get_or_create(phone=phone)
        return customer_dto.to_entity()

    def get(self, phone: str) -> CustomerEntity:
        customer_dto = Customer.objects.get(phone=phone)
        return customer_dto.to_entity()

    def generate_token(self, customer: CustomerEntity) -> str:
        token = str(uuid4())
        Customer.objects.filter(phone=customer.phone).update(
            token=token,
        )
        return token
