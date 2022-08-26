import re

from .exceptions import SpendingParseError
from .models import Category, Spending


def parse_spending(text):
    if not re.match(r'^/spend ([\d]+) ', text):
        raise SpendingParseError

    _, amount, category_name = text.split(maxsplit=2)
    return {
        'amount': int(amount),
        'category_name': category_name,
    }


async def create_spending(amount, category_name):
    category = await _get_or_create_category(category_name)
    return await Spending.create(category=category, amount=amount)


async def _get_or_create_category(category_name):
    category, _ = await Category.get_or_create(name=category_name)
    return category
