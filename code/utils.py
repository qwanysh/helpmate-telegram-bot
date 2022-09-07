from datetime import datetime, timedelta
import re

from tortoise.functions import Sum

from .exceptions import SpendingAmountError, SpendingFormatError
from .models import Category, Spending


def parse_spending(text):
    if not re.match(r'^/spend ([\d]+) ', text):
        raise SpendingFormatError

    _, amount, category_name = text.split(maxsplit=2)
    amount = int(amount)

    if amount <= 0:
        raise SpendingAmountError

    return {
        'amount': amount,
        'category_name': category_name,
    }


async def create_spending(amount, category_name):
    category, _ = await Category.get_or_create(name=category_name)
    return await Spending.create(category=category, amount=amount)


async def get_today_spendings_by_categories():
    today = datetime.utcnow().date()
    return (
        await Spending
        .filter(
            created_at__gte=today,
            created_at__lt=today + timedelta(days=1),
        )
        .annotate(total=Sum('amount'))
        .group_by('category__name')
        .order_by('-total')
        .values('category__name', 'total')
    )
