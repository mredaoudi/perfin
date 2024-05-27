from django.db.models import (
    F,
    Sum,
    Model,
    CASCADE,
    SET_NULL,
    CharField,
    DateField,
    ForeignKey,
    BooleanField,
    DecimalField,
)
from django.utils import timezone
from django.contrib.auth import get_user_model
from .validators import validate_non_zero_amount

User = get_user_model()


class Account(Model):
    name = CharField(max_length=255, unique=True)
    is_saving = BooleanField(default=False)
    initial_amount = DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    start_date = DateField(default=timezone.now)
    user = ForeignKey(User, on_delete=CASCADE)

    def current_amount(self):
        transactions = self.transactions.all()
        secondary_transactions = self.secondary_transactions.all()
        amount = self.initial_amount
        if transactions.exists():
            amount += transactions.aggregate(total=Sum('amount'))['total']
        if secondary_transactions.exists():
            amount += secondary_transactions.aggregate(
                total=Sum(-F('amount'))
            )['total']
        return amount

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Category(Model):
    name = CharField(max_length=255, unique=True)

    def total_amount(self, user):
        return Transaction.objects.filter(
            entity__category=self,
            account__user=user
        ).aggregate(total_amount=Sum('amount'))['total_amount']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']


class Entity(Model):
    name = CharField(max_length=255, unique=True)
    category = ForeignKey(
        Category,
        on_delete=SET_NULL,
        blank=True,
        null=True
    )
    is_person = BooleanField(default=False)
    user = ForeignKey(User, on_delete=CASCADE)

    def amount_spent(self):
        transactions = self.transaction_set.all()
        if transactions.exists():
            return transactions.aggregate(total=Sum('amount'))['total']
        return 0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "entities"
        ordering = ['name']


class Transaction(Model):
    account = ForeignKey(
        Account,
        on_delete=CASCADE,
        related_name='transactions'
    )
    amount = DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_non_zero_amount]
    )
    entity = ForeignKey(
        Entity,
        on_delete=SET_NULL,
        blank=True,
        null=True
    )
    other_account = ForeignKey(
        Account,
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name='secondary_transactions'
    )
    transaction_date = DateField(default=timezone.now)

    def __str__(self):
        direction = 'to' if self.amount < 0 else 'from'
        return f'{self.amount} {direction} {self.entity}'

    class Meta:
        ordering = ['-transaction_date']
