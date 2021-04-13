from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from .models import Wallet, Transaction
import json
import os

basedir = os.path.dirname(os.path.realpath(__file__))


def index(request):
    return HttpResponse(open(os.path.join(basedir, 'templates/index.html')))


def create_wallet(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['wallet_name']
        wallet = Wallet(name=name)
        wallet.save()

        return JsonResponse({'name': wallet.name})

    return HttpResponse(status=405)


def edit_wallet(request, name):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        new_name = body['new_wallet_name']
        wallet = Wallet.objects.get(name=name)
        wallet.name = new_name
        wallet.save()

        return JsonResponse({'new_name': new_name})

    return HttpResponse(status=405)


def delete_wallet(request, name):
    if request.method == "DELETE":
        Wallet.objects.filter(name=name).delete()

        return JsonResponse({'status': 'deleted'})

    return HttpResponse(status=405)


def credit_balance(request, name):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        sum = int(body['credit_sum'])
        comment = body['comment']
        wallet = Wallet.objects.get(name=name)
        transaction = Transaction(sum=sum, comment=comment, wallet=wallet)
        transaction.save()

        return JsonResponse({'wallet_balance_changed': wallet.name})

    return HttpResponse(status=405)


def debit_balance(request, name):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        sum = -int(body['debit_sum'])
        comment = body['comment']
        wallet = Wallet.objects.get(name=name)
        transaction = Transaction(sum=sum, comment=comment, wallet=wallet)
        transaction.save()

        return JsonResponse({'wallet_balance_changed': wallet.name})

    return HttpResponse(status=405)


def get_wallet_list(request):
    if request.method == "GET":
        wallet_list = Wallet.objects.all().values("name")

        return JsonResponse({"wallet_list": list(wallet_list)})

    return HttpResponse(status=405)


def get_all_transactions(request):
    if request.method == "GET":
        query_set = Transaction.objects.select_related("wallet").all()
        transactions = []
        for transaction in query_set:
            transactions.append(
                {'id': transaction.id, 'wallet_name': transaction.wallet.name, 'datetime': transaction.datetime,
                 'sum': transaction.sum, 'comment': transaction.comment})
        return JsonResponse({"all_transactions": transactions})

    return HttpResponse(status=405)


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

    return HttpResponse(status=405)


def delete_transaction(request):
    if request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        transaction_id = int(body['transaction_id'])
        Transaction.objects.filter(id=transaction_id).delete()
        return JsonResponse({'status': 'deleted'})

    return HttpResponse(status=405)


def get_wallet_balance(request, name):
    if request.method == "GET":
        wallet = Wallet.objects.get(name=name)
        balance = Transaction.objects.filter(wallet_id=wallet.id).aggregate(wallet_balance=Sum('sum'))
        return JsonResponse({"wallet_balance": balance['wallet_balance']})

    return HttpResponse(status=405)


def get_total_balance(request):
    if request.method == "GET":
        balance = Transaction.objects.all().aggregate(total_balance=Sum('sum'))
        return JsonResponse({"total_balance": balance['total_balance']})

    return HttpResponse(status=405)
