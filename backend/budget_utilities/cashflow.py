from typing import TypeAlias

from django.db.models import Sum
from django.db.models.base import Model

from backend.models import Income, Expense

Transaction: TypeAlias = Income | Expense


def get_most_recent_transactions(transaction_type: type[Transaction], number_of_operations: int = 5) -> list[Model]:
    return transaction_type.objects.all().order_by("-date")[:number_of_operations]


def get_total_of_transaction_type(transaction_type: type[Transaction]) -> float:
    return transaction_type.objects.aggregate(total=Sum("amount"))["total"] or 0.0
