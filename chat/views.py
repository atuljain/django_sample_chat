from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
 
from chat.models import ChatRoom
# Create your views here.
def index(request):
	chat_room = ChatRoom.objects.order_by('name')[:5]
	context = {
		'chat_list': chat_room,
		}
	return render(request, 'chat/index.html', context)
def chat_room(request, id):
	print id
	chat = get_object_or_404(ChatRoom, pk=id)
	return render(request, 'chat/chat_room.html', {'chat':chat})

	
