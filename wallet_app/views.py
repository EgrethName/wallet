import json
import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Sum

from .models import Wallet, Transaction


basedir = os.path.dirname(os.path.realpath(__file__))


def index(request):
    return HttpResponse(open(os.path.join(basedir, 'templates/index.html')))


@require_http_methods(["GET", "POST"])
def wallets_handler(request):
    if request.method == "GET":
        wallet_list = Wallet.objects.all().values("name")
        return JsonResponse({"wallets": list(wallet_list)})
    elif request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['name']
        wallet = Wallet(name=name)
        wallet.save()
        return JsonResponse({'name': wallet.name})


@require_http_methods(["POST", "DELETE"])
def change_wallet(request, name):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        new_name = body['new_name']
        wallet = Wallet.objects.get(name=name)
        wallet.name = new_name
        wallet.save()
        return JsonResponse({'new_name': new_name})
    elif request.method == "DELETE":
        Wallet.objects.filter(name=name).delete()
        return HttpResponse(status=204)


@require_http_methods(["POST"])
def credit_balance(request, name):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        credit_sum = float(body['sum'])
        comment = body['comment']
        wallet = Wallet.objects.get(name=name)
        transaction = Transaction(sum=credit_sum, comment=comment, wallet=wallet)
        transaction.save()
        return HttpResponse(status=200)


@require_http_methods(["POST"])
def debit_balance(request, name):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        debit_sum = -float(body['sum'])
        comment = body['comment']
        wallet = Wallet.objects.get(name=name)
        transaction = Transaction(sum=debit_sum, comment=comment, wallet=wallet)
        transaction.save()
        return HttpResponse(status=200)


@require_http_methods(["GET"])
def get_all_transactions(request):
    if request.method == "GET":
        query_set = Transaction.objects.select_related("wallet").all()
        transactions = []
        for transaction in query_set:
            transactions.append(
                {'id': transaction.id, 'wallet_name': transaction.wallet.name, 'datetime': transaction.datetime,
                 'sum': transaction.sum, 'comment': transaction.comment})
        return JsonResponse({"all_transactions": transactions})


@require_http_methods(["GET"])
def get_wallet_transaction(request, name):
    if request.method == "GET":
        wallet = Wallet.objects.get(name=name)
        query_set = Transaction.objects.select_related("wallet").filter(wallet_id=wallet.id)
        transactions = []
        for transaction in query_set:
            transactions.append(
                {'id': transaction.id, 'wallet_name': transaction.wallet.name, 'datetime': transaction.datetime,
                 'sum': transaction.sum, 'comment': transaction.comment})
        return JsonResponse({"wallet_transactions": transactions})


@require_http_methods(["DELETE"])
def delete_transaction(request, name, transaction_id):
    if request.method == "DELETE":
        Transaction.objects.filter(id=transaction_id).delete()
        return HttpResponse(status=204)


@require_http_methods(["GET"])
def get_wallet_balance(request, name):
    if request.method == "GET":
        wallet = Wallet.objects.get(name=name)
        balance = Transaction.objects.filter(wallet_id=wallet.id).aggregate(wallet_balance=Sum('sum'))
        return JsonResponse({"wallet_balance": balance['wallet_balance']})


@require_http_methods(["GET"])
def get_total_balance(request):
    if request.method == "GET":
        balance = Transaction.objects.all().aggregate(total_balance=Sum('sum'))
        return JsonResponse({"total_balance": balance['total_balance']})
