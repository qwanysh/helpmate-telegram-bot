from tortoise import fields, Model


class Category(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'categories'


class Spending(Model):
    id = fields.UUIDField(pk=True)
    category = fields.ForeignKeyField(
        'models.Category', related_name='spendings',
    )
    amount = fields.IntField()
    created_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'spendings'
