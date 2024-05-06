from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    """
    Represents a chat room.

    Attributes:
        name (str): The name of the room.
    """
    name = models.CharField(max_length=1000)
class Message(models.Model):
    """
    Represents a chat message.

    Attributes:
        value (str): The content of the message.
        date (datetime): The date and time when the message was sent.
        user (str): The username of the user who sent the message.
        room (str): The name of the chat room where the message was sent.
    """
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)