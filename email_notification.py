from .notification_sender import NotificationSender


class EmailNotification(NotificationSender):
    def __init__(self, recipient: str, smtp_server: str = "smtp.gmail.com"):
        super().__init__(recipient)
        self.smtp_server = smtp_server

    def send(self, message: str) -> str:
        return f"Email отправлен на {self._recipient} через {self.smtp_server}: \"{message}\""
