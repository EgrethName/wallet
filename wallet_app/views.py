from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Wallet
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


