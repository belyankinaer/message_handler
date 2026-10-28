from abc import ABC, abstractmethod


class NotificationSender(ABC):
    def __init__(self, recipient: str):
        self._recipient = recipient

    @abstractmethod
    def send(self, message: str) -> str:
        ...
