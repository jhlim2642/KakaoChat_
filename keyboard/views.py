from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def keyboard_(request):
    return JsonResponse({'type':'buttons',
                        'buttons':['select1','select2','select3']
})

#json_str = ((request.body).decode('utf-8'))
#received_json_data = json.loads(json_str)