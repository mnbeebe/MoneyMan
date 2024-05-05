from django.shortcuts import render
from django.views.generic import ListView
from .models import Expense
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(ListView, LoginRequiredMixin):
    template_name = "ExpenseTracker/index.html"
    context_object_name = "expense_list"

    def get_queryset(self):
        """
        Return all expenses
        """
        return Expense.objects.all()
    