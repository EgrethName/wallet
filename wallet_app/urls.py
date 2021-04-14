from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wallets', views.wallets_handler, name='wallets_handler'),
    path('wallets/all_transactions', views.get_all_transactions, name='all_transactions'),
    path('wallets/total_balance', views.get_total_balance, name='total_balance'),
    re_path(r'wallets/(?P<name>\S+)/balance', views.get_wallet_balance, name='get_balance'),
    re_path(r'wallets/(?P<name>\S+)/transactions/credit', views.credit_balance, name='credit_balance'),
    re_path(r'wallets/(?P<name>\S+)/transactions/debit', views.debit_balance, name='debit_balance'),
    re_path(r'wallets/(?P<name>\S+)/transactions/(?P<transaction_id>\d+)', views.delete_transaction,
            name='delete_transaction'),
    re_path(r'wallets/(?P<name>\S+)/transactions', views.get_wallet_transaction, name='get_transactions'),
    re_path(r'wallets/(?P<name>\S+)', views.change_wallet, name='change_wallet'),
]
