class SftpUtilException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def getMessage(self):
        return self.message.get('message')