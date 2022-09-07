import pytest

from code.exceptions import SpendingAmountError, SpendingFormatError
from code.utils import parse_spending


@pytest.mark.parametrize('text, amount, category_name', [
    ('/spend 1000 food', 1000, 'food'),
    ('/spend 2000 tasty food', 2000, 'tasty food'),
])
def test_parse_spending_success(text, amount, category_name):
    expected = {
        'amount': amount,
        'category_name': category_name,
    }

    assert parse_spending(text) == expected


@pytest.mark.parametrize('text, exception', [
    ('/spend', SpendingFormatError),
    ('/spend 1000', SpendingFormatError),
    ('/spend -1000', SpendingFormatError),
    ('/spend food food', SpendingFormatError),
    ('/spend 0 food', SpendingAmountError),
])
def test_parse_spending_failure(text, exception):
    with pytest.raises(exception):
        parse_spending(text)
