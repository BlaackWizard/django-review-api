from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.apps.customers.services.codes import BaseCodeServices
from core.apps.customers.services.customers import BaseCustomerServices
from core.apps.customers.services.senders import BaseSendersServices


@dataclass(eq=False)
class BaseAuthServices(ABC):
    customer_service: BaseCustomerServices
    code_service: BaseCodeServices
    sender_service: BaseSendersServices
    @abstractmethod
    def authorize(self, phone: str):
        ...

    @abstractmethod
    def confirm(self, code: str, phone: str):
        ...

class AuthService(BaseAuthServices):
    def authorize(self, phone: str):
        customer = self.customer_service.get_or_create(phone)
        code = self.code_service.generate_code(customer)
        self.sender_service.send_code(code)
    def confirm(self, code: str, phone: str):
        customer = self.customer_service.get(phone)
        self.code_service.validate_code(code, customer)
        return self.customer_service.generate_token(customer)
