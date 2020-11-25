from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=true)
    host = models.CharField(max_length=80, unique=true)
    guest_can_pause = models.BooleanField(null=false, default=false)
    votes_to_skip = models.IntegerField(null=false, default=1)
    created_at = models.DateTimeField(auto_now_add=true)


