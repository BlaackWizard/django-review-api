from abc import ABC, abstractmethod

from core.apps.customers.entities import CustomerEntity


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