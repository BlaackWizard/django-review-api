from abc import (
    ABC,
    abstractmethod,
)

from core.apps.customers.entities import CustomerEntity


class BaseSendersServices(ABC):
    @abstractmethod
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        ...


class DummySenderServices(BaseSendersServices):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code to user: {customer}, sent: {code}")
