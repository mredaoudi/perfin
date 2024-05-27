from decimal import Decimal
from django.core.exceptions import ValidationError


def validate_non_zero_amount(value):
    if value == Decimal('0'):
        raise ValidationError('Amount must be non-zero.')

    if not (Decimal('0.01') <= abs(value) < Decimal('inf')):
        raise ValidationError('Amount must be greater than 0.01 or less than -0.01.')
