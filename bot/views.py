from django.http import JsonResponse
from .models import UserMessage
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        msg = UserMessage.objects.create(
            user_id=data['user_id'], message_text=data['message_text']
        )
        return JsonResponse({'id': msg.id, 'message': 'Created successfully!'})

def read_messages(request):
    messages = list(UserMessage.objects.values())
    return JsonResponse(messages, safe=False)

@csrf_exempt
def update_message(request, message_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        msg = UserMessage.objects.get(id=message_id)
        msg.message_text = data['message_text']
        msg.save()
        return JsonResponse({'message': 'Updated successfully!'})

@csrf_exempt
def delete_message(request, message_id):
    if request.method == 'DELETE':
        msg = UserMessage.objects.get(id=message_id)
        msg.delete()
        return JsonResponse({'message': 'Deleted successfully!'})

