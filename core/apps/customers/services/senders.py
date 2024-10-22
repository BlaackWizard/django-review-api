from abc import abstractmethod, ABC


class BaseSendersServices(ABC):
    @abstractmethod
    def send_code(self, code: str) -> None:
        ...
