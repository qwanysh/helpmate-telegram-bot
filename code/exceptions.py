class MessageError(Exception):
    message = None


class SpendingParseError(MessageError):
    message = 'Spending in wrong format'
