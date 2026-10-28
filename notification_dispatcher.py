from .notification_sender import NotificationSender


class NotificationDispatcher:
    def __init__(self):
        self._senders: list[NotificationSender] = []

    def add_sender(self, sender: NotificationSender) -> None:
        self._senders.append(sender)

    def dispatch(self, message: str) -> list[str]:
        return [sender.send(message) for sender in self._senders]
