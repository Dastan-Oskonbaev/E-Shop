from django.shortcuts import render
from django.views.generic import CreateView
from .models import Account
from .forms import AccountForm


class AccountView(CreateView):
    model = Account
    form_class = AccountForm
    success_url = "/"

