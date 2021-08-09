from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model() 

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=250, default=None)

    
    def __str__(self):
        return self.room

    def last_10_messages(room_name):
        mesages_of_room = Message.objects.filter(room = room_name)
        return mesages_of_room.order_by('timestamp').all()[:10]
