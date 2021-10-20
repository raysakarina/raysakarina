
from django.http import HttpResponse

from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('La hora actual del servidor es {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = 'Lo siento {}, no tienes permiso'.format(name)
    else:
        message = 'Hola tu, {}!'.format(name)
    return HttpResponse(message)