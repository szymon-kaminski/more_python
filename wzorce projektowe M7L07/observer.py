class Subject:
    def __init__(self):
        self._observers = []

    
    def attach(self, observer):
        self._observers.append(observer)

    
    def detach(self, observer):
        self._observers.remove(observer)

    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        pass


class EmailSubscriber(Observer):
    def update(self, message):
        print(f"Email received: {message}")


class SmsSubscriber(Observer):
    def update(self, message):
        print(f"SMS recived: {message}")


def main():
    subject = Subject()

    email = EmailSubscriber()
    sms = SmsSubscriber()

    subject.attach(email)
    subject.attach(sms)

    subject.notify("A new video is up - check it out!")


if __name__ == "__main__":
    main()
