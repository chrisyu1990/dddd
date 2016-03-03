from django.shortcuts import render
from django.utils import timezone
from .models import Session
from .models import Beacon
from .models import Speaker
from django.core import serializers
from .models import Attendee
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# Create your views here.
def session_list(request): 
	result = "["
	sessions = Session.objects.all()
	for session in sessions:
		result += session.asjson() 
		result += ","
	#results[-1] = ""#results[:-1]
	result = result[0:-1] + "]"
	return HttpResponse(result, content_type='application/json')

	#data = serializers.serialize("json", Session.objects.all())
	#return render(request, 'hac/session_list.html', {'data': Session.objects.all()})

def beacon_list(request):    
	result = "["
	sessions = Beacon.objects.all()
	for session in sessions:
		result += session.asjson()
		result += ","
        #results[-1] = ""#results[:-1]
	result = result[0:-1] + "]"
	return HttpResponse(result, content_type='application/json')
	#data = serializers.serialize("json", Beacon.objects.all())
	#return render(request, 'hac/beacon_list.html', {'data': Beacon.objects.all()})

@csrf_exempt
def post_new_attendee(request):    
    if request.method == "POST":
    	response_json = request.body.decode('utf-8')
    	dataform = str(response_json).strip("'<>() ").replace('\'', '\"')
    	received_json_data = json.loads(dataform)
        #received_json_data = json.loads(request.body.decode('utf-8'))
    	attendee = Attendee()
    	attendee.name = received_json_data['name']
    	attendee.corpId = received_json_data['corpId']
    	attendee.device_type = received_json_data['device_type']
    	attendee.app_version = received_json_data['app_version']
    	attendee.ibeacon_uuid = received_json_data['ibeacon_uuid']
    	attendee.major_id = received_json_data['major_id']
    	attendee.minor_id = received_json_data['minor_id']
    	attendee.date = timezone.now() 
    	attendee.created_date = timezone.now()
    	
    	print ("attendee : " + attendee.name + " " + attendee.corpId) 
    	attendee.save()
    	return HttpResponse('Hello world')
        #return 'Raw Data: "%s"' % request.body   
        #form = PostForm(request.POST)
        #if form.is_valid():
        #    post = form.save(commit=False)
        #    post.author = request.user
        #    post.published_date = timezone.now()
        #    post.save()
        #    return "done"
    else:
    	return "failure"
    return "falure"

