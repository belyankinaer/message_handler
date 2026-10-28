from .notification_sender import NotificationSender


class MessengerNotification(NotificationSender):
    def __init__(self, recipient: str, platform: str = "Telegram"):
        super().__init__(recipient)
        self._platform = platform

    def send(self, message: str) -> str:
        return f"Сообщение отправлено через {self._platform} пользователю {self._recipient}: \"{message}\""
