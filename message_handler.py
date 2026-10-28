from .email_notification import EmailNotification
from .messenger_notification import MessengerNotification
from .notification_dispatcher import NotificationDispatcher
from .sms_notification import SMSNotification

if __name__ == "__main__":
    dispatcher = NotificationDispatcher()

    dispatcher.add_sender(EmailNotification("user@example.com"))
    dispatcher.add_sender(SMSNotification("+79001234567"))
    dispatcher.add_sender(MessengerNotification("@ivanov", "Telegram"))

    results = dispatcher.dispatch("Встреча перенесена на 15:00")

    for result in results:
        print(result)
