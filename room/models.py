from django.contrib.auth.models import User
from django.db import models

# Create your models here.
VISIBILITY_CHOICES = [("1", 'public',), ("2", 'private',)]


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    members = models.ManyToManyField(User, related_name="rooms", default=None)
    creator = models.ForeignKey(User, related_name='created_rooms', on_delete=models.DO_NOTHING, null=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Message(models.Model):

    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('date_added',)


# class friends(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
#     friend = models.ForeignKey(User, related_name='friends_friend', on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('date_added',)
#         unique_together = ('user', 'friend')
#         verbose_name = 'friend'
#         verbose_name_plural = 'friends'