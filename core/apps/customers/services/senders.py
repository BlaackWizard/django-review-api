from abc import (
    ABC,
    abstractmethod,
)


class BaseSendersServices(ABC):
    @abstractmethod
    def send_code(self, code: str) -> None:
        ...
