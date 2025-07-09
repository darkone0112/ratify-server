from django.urls import path
from .views import add_expense, get_month_expenses

urlpatterns = [
    path('add/', add_expense, name='add_expense'),
    path('month/', get_month_expenses, name='get_month_expenses'),
] 