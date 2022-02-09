from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    recipient 		= models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'recipient')
    sender 			= models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sender')
    body	 		= models.TextField()
    sent 			= models.DateTimeField(auto_now_add = True)
    unread 			= models.BooleanField(default = True)

    def __str__(self):
        return 'Message from ' + str(self.sender) + '.  Subject:' + str(self.body)