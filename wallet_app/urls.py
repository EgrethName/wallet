"""wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_wallet', views.create_wallet, name='new_wallet'),
    path('all_wallets', views.get_wallet_list, name='all_wallets'),
    path('all_transactions', views.get_all_transactions, name='all_transactions'),
    path('delete_transaction', views.delete_transaction, name='delete_transaction'),
    path('total_balance', views.get_total_balance, name='total_balance'),
    re_path(r'(?P<name>\S+)/edit', views.edit_wallet, name='edit_wallet'),
    re_path(r'(?P<name>\S+)/delete', views.delete_wallet, name='delete_wallet'),
    re_path(r'(?P<name>\S+)/credit', views.credit_balance, name='credit_balance'),
    re_path(r'(?P<name>\S+)/debit', views.debit_balance, name='debit_balance'),
    re_path(r'(?P<name>\S+)/get_transactions', views.get_wallet_transaction, name='get_transactions'),
    re_path(r'(?P<name>\S+)/get_balance', views.get_wallet_balance, name='get_balance'),
]
