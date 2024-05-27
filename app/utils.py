from django.db.models import Sum, F
from django.db.models.functions import TruncMonth, ExtractYear
from .models import Transaction


def get_transactions_grouped_by_month(year=None, queryset=None):
    if queryset is None:
        print("check")
        queryset = Transaction.objects.all()

    queryset = queryset.annotate(
        month=TruncMonth('transaction_date')
    )
    print([q.month.strftime('%B') for q in queryset])

    if year:
        queryset = queryset.annotate(
            year=ExtractYear('transaction_date')
        ).filter(year=year)

    transactions_by_month = queryset.values('month').annotate(
        total_amount=Sum(-(F('amount')))
    ).order_by('month')

    return transactions_by_month
