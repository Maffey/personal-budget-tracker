from django.db import models

# For user authentication
# from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    """
    Represents a category for transactions (both income and expense).
    Examples: Groceries, Salary, Rent, Entertainment.
    """

    name = models.CharField(max_length=100, unique=True, help_text="Name of the category (e.g., Groceries, Salary)")
    description = models.TextField(blank=True, null=True, help_text="Description for the category")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    """
    Represents the method of payment for an expense.
    Examples: Credit Card A, Debit Card B, Cash, Bank Transfer.
    """

    name = models.CharField(
        max_length=100, unique=True, help_text="Name of the payment method (e.g., Credit Card XYZ, Cash)"
    )
    description = models.TextField(blank=True, null=True, help_text="Description for the payment method")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class IncomeSource(models.Model):
    """
    Represents the source of an income.
    Examples: Employer A, Freelance Project X, Investment Y.
    """

    name = models.CharField(
        max_length=100, unique=True, help_text="Name of the income source (e.g., Main Job, Freelance Client)"
    )
    description = models.TextField(blank=True, null=True, help_text="Description for the income source")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Expense(models.Model):
    """
    Represents an expense transaction.
    """

    # For user authentication:
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="expenses")
    description = models.CharField(max_length=255, help_text="Brief description of the expense")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount spent")
    date = models.DateField(default=timezone.now, help_text="Date of the expense")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses",
        help_text="Category of the expense",
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses",
        help_text="How this expense was paid",
    )
    notes = models.TextField(blank=True, null=True, help_text="Additional notes for the expense")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]  # Show newest expenses first

    def __str__(self):
        return f"{self.description} - {self.amount} on {self.date.strftime('%Y-%m-%d')}"


class Income(models.Model):
    """
    Represents an income transaction.
    """

    # For user authentication:
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="incomes")
    description = models.CharField(max_length=255, help_text="Brief description of the income")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount received")
    date = models.DateField(default=timezone.now, help_text="Date the income was received")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incomes",
        help_text="Category of the income (e.g., Salary, Bonus)",
    )
    source = models.ForeignKey(
        IncomeSource,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incomes",
        help_text="Source of this income",
    )
    notes = models.TextField(blank=True, null=True, help_text="Additional notes for the income")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]  # Show newest incomes first

    def __str__(self):
        return f"{self.description} - {self.amount} on {self.date.strftime('%Y-%m-%d')}"
