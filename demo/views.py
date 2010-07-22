from django.http import HttpResponse
from django.utils import simplejson
from django.utils.translation import ugettext

from push_demo.push.models import iPhone, sendMessageToPhoneGroup

def json_response(func):
    def wrap(*args, **kwargs):

        response = None

        try:
            response = func(*args, **kwargs)
            assert isinstance(response, dict)
        except Exception, e:
            if hasattr(e, 'message'):
                msg = e.message
            else:
                msg = ugettext('Internal error') + ': ' + str(e)
            response = {'result': 'error',
                        'text': e}

        json = simplejson.dumps(response)

        return HttpResponse(json, mimetype='application/json')
    return wrap

@json_response
def registerDevice(request):
    udid = request.REQUEST.get('udid')

    device = iPhone(udid = udid)
    device.save();

    return {'code': '200', 'result': 'Success'}

@json_response
def sendNotificationToDevice(request):
    udid         = request.REQUEST.get('udid')
    notification = request.REQUEST.get('notification')
        
    try:
        device = iPhone.objects.get(udid = udid)
        device.send_message(alert = notification)
    except iPhone.DoesNotExist:
        return {'code': '404', 'result': 'Device not found'}

    return {'code': '200', 'result': 'Success'}

@json_response
def sendNotificationToAllDevices(request):
    notification = request.REQUEST.get('notification')
    device_list  = iPhone.objects.all()

    if not device_list:
        return {'code': '405', 'result': 'No devices!'}

    sendMessageToPhoneGroup(phone_list = device_list, alert = notification)
    
    return {'code': '200', 'result': 'Success'}
