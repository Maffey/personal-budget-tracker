from django.contrib import admin

from backend.models import Income, Expense, IncomeSource, PaymentMethod, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(IncomeSource)
class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "amount",
        "date",
        "category",
        "payment_method",
        "display_user",
    )  # 'user' if you uncommented it
    list_filter = ("date", "category", "payment_method")  # 'user'
    search_fields = ("description", "notes", "category__name", "payment_method__name")  # 'user__username'
    date_hierarchy = "date"
    ordering = ("-date",)
    readonly_fields = ("created_at", "updated_at")

    # If you had the user field active:
    # def display_user(self, obj):
    #     return obj.user.username if obj.user else "N/A"
    # display_user.short_description = 'User'

    def display_user(self, obj):
        if hasattr(obj, "user") and obj.user:
            return obj.user.username
        return "N/A (Single User Mode)"

    display_user.short_description = "User (if applicable)"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "description",
                    "amount",
                    "date",
                    "category",
                    "payment_method",
                    "notes",
                )  # Add 'user' here if active
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "amount",
        "date",
        "category",
        "source",
        "display_user",
    )  # 'user' if you uncommented it
    list_filter = ("date", "category", "source")  # 'user'
    search_fields = ("description", "notes", "category__name", "source__name")  # 'user__username'
    date_hierarchy = "date"
    ordering = ("-date",)
    readonly_fields = ("created_at", "updated_at")

    # If you had the user field active:
    # def display_user(self, obj):
    #     return obj.user.username if obj.user else "N/A"
    # display_user.short_description = 'User'

    def display_user(self, obj):
        if hasattr(obj, "user") and obj.user:
            return obj.user.username
        return "N/A (Single User Mode)"

    display_user.short_description = "User (if applicable)"

    fieldsets = (
        (
            None,
            {
                "fields": ("description", "amount", "date", "category", "source", "notes")  # Add 'user' here if active
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
