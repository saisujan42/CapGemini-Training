class Notification:
    def send(self, notification_type):
        print()
        print(f"You Have A {notification_type} Notification : ")

class EmailNotification(Notification):
    def send(self, message):
        super().send("Email")
        print(message)

class SMSNotification(Notification):
    def send(self, message):
        super().send("SMS")
        print(message)

def main():
    email = EmailNotification()
    sms = SMSNotification()

    email.send("You Have a Sign-In from Different Device.")
    sms.send("$100.87 Credited into Your Account.")
main()