from .notification_sender import NotificationSender


class SMSNotification(NotificationSender):
    def __init__(self, recipient: str, carrier: str = "MTS"):
        super().__init__(recipient)
        self._carrier = carrier

    def send(self, message: str) -> str:
        return f"SMS отправлено на {self._recipient} через {self._carrier}: \"{message}\""
