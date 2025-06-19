from django.utils import timezone


def get_current_month() -> str:
    return timezone.now().strftime("%B %Y")
