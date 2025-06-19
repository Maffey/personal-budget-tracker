# backend/views.py
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .budget_utilities.cashflow import get_most_recent_transactions, get_total_of_transaction_type
from .budget_utilities.date_time import get_current_month
from .models import Category, PaymentMethod, Expense, Income
from .forms import CategoryForm, PaymentMethodForm, ExpenseForm, IncomeForm


def home(request: HttpRequest) -> HttpResponse:
    """
    A simple dashboard showing recent transactions and summaries.
    """
    recent_expenses = get_most_recent_transactions(Expense)
    recent_incomes = get_most_recent_transactions(Income)

    total_expense = get_total_of_transaction_type(Expense)
    total_income = get_total_of_transaction_type(Income)
    net_balance = total_income - total_expense

    context = {
        "recent_expenses": recent_expenses,
        "recent_incomes": recent_incomes,
        "total_expense": total_expense,
        "total_income": total_income,
        "net_balance": net_balance,
        "current_month": get_current_month(),
    }
    return render(request, "backend/home.html", context)


def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, "backend/category_list.html", {"categories": categories})


def category_detail(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    category_expenses = category.expenses.all()
    category_incomes = category.incomes.all()
    return render(
        request,
        "backend/category_detail.html",
        {"category": category, "expenses": category_expenses, "incomes": category_incomes},
    )


def category_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("backend:category_list")
    else:
        form = CategoryForm()
    return render(request, "backend/category_form.html", {"form": form, "form_title": "Create Category"})


def category_update(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("backend:category_detail", pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, "backend/category_form.html", {"form": form, "form_title": "Update Category"})


def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("backend:category_list")
    return render(request, "backend/category_confirm_delete.html", {"object": category, "type": "Category"})


class ExpenseListView(ListView):
    model = Expense
    template_name = "backend/expense_list.html"
    context_object_name = "expenses"
    paginate_by = 10


class ExpenseDetailView(DetailView):
    model = Expense
    template_name = "backend/expense_detail.html"
    context_object_name = "expense"


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "backend/expense_form.html"
    success_url = reverse_lazy("backend:expense_list")  # Redirect after successful creation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Add New Expense"
        return context


class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = "backend/expense_form.html"
    success_url = reverse_lazy("backend:expense_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Update Expense"
        return context


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = "backend/expense_confirm_delete.html"
    success_url = reverse_lazy("backend:expense_list")
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Expense"
        return context


class IncomeListView(ListView):
    model = Income
    template_name = "backend/income_list.html"
    context_object_name = "incomes"
    paginate_by = 10


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = "backend/income_form.html"
    success_url = reverse_lazy("backend:income_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Add New Income"
        return context


# .TODO IncomeDetailView, IncomeUpdateView, IncomeDeleteView ...


class PaymentMethodListView(ListView):
    model = PaymentMethod
    template_name = "backend/paymentmethod_list.html"
    context_object_name = "payment_methods"


class PaymentMethodCreateView(CreateView):
    model = PaymentMethod
    form_class = PaymentMethodForm
    template_name = "backend/paymentmethod_form.html"
    success_url = reverse_lazy("backend:paymentmethod_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Add Payment Method"
        return context
