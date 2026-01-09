from django.db.models.fields import return_None
from django.http import JsonResponse
from django.shortcuts import render

def users(request):
    if request.method == 'GET':
        user={
            'id':1,
            'nome': 'Gabriel'
        }

        # considerar como estar no objeto ( podendo haver caracterares especiais )
    return JsonResponse(user, json_dumps_params={'ensure_ascii':False})
