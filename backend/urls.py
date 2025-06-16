from django.urls import path

from backend import views

urlpatterns = [
    path("", views.home, name="home"),
    # Category URLs (FBV examples)
    path("categories/", views.category_list, name="category_list"),
    path("categories/new/", views.category_create, name="category_create"),
    path("categories/<int:pk>/", views.category_detail, name="category_detail"),
    path("categories/<int:pk>/edit/", views.category_update, name="category_update"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),
    # Expense URLs (CBV examples)
    path("expenses/", views.ExpenseListView.as_view(), name="expense_list"),
    path("expenses/new/", views.ExpenseCreateView.as_view(), name="expense_create"),
    path("expenses/<int:pk>/", views.ExpenseDetailView.as_view(), name="expense_detail"),
    path("expenses/<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="expense_update"),
    path("expenses/<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="expense_delete"),
    # Income URLs (CBV examples - showing a couple)
    path("incomes/", views.IncomeListView.as_view(), name="income_list"),
    path("incomes/new/", views.IncomeCreateView.as_view(), name="income_create"),
    # ... add detail, update, delete URLs for Income as well
    # PaymentMethod URLs (CBV examples - showing a couple)
    path("payment-methods/", views.PaymentMethodListView.as_view(), name="paymentmethod_list"),
    path("payment-methods/new/", views.PaymentMethodCreateView.as_view(), name="paymentmethod_create"),
]
