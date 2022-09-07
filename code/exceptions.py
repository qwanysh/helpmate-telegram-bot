class MessageError(Exception):
    message = None


class SpendingFormatError(MessageError):
    message = 'Spending in wrong format'


class SpendingAmountError(MessageError):
    message = "Spending amount can't be negative"
