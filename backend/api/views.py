import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    
    print(request.GET)
    
    data = {}
    
    try:
        data = json.loads(request.body)
    except:
        pass
        
    return JsonResponse({
        "data": "Hello World",
        "body": data
    })
