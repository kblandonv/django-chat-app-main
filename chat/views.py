from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered home.html template.
    """
    return render(request, 'home.html')

def room(request, room):
    """
    Renders the chat room page.

    Args:
        request (HttpRequest): The HTTP request object.
        room (str): The name of the chat room.

    Returns:
        HttpResponse: The rendered chat room page.

    Raises:
        Room.DoesNotExist: If the specified chat room does not exist.
    """
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    """
    This view function checks if a room exists in the database. If the room exists, it redirects the user to the room page
    with the provided username. If the room doesn't exist, it creates a new room in the database and redirects the user
    to the room page with the provided username.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect response to the room page with the provided username.
    """
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    """
    Sends a message to a chat room.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response indicating the success of the message sending.

    Raises:
        KeyError: If any of the required POST parameters are missing.

    """
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    """
    Retrieve messages for a specific room.

    Args:
        request (HttpRequest): The HTTP request object.
        room (str): The name of the room.

    Returns:
        JsonResponse: A JSON response containing the messages for the room.
    """
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
