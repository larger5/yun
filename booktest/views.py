# -*- coding:utf-8 -*-
from .models import *

from django.http import JsonResponse

# 6.返回 json 字符串
def getJson(request):
    temp = BookInfo.objects.all()
    data = []
    # 必须全为字典的格式
    for a in temp:
        data.append({'id': a.id, 'title': a.btitle,"bpub_date": a.bpub_date})
    return JsonResponse({'data': data} )