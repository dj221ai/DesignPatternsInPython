'''
    1. Dependency Inversion Principle aka DIP states that the high level modules should not depend on low level modules instead both modules should depend on abstractions
    2. Direct dependencies on concrete classes makes it more harder to change or extend in short makes it less flexible.    
'''

from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass


class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"sending sms {message} to {receiver}")


class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"sending email {message} to {receiver}")


class NotificationService:
    def __init__(self, message_service:IMessageService):
        self.message_service=message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)



