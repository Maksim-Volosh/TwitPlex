from django.db import models

from user.models import User

class Tweets(models.Model):
    tweet = models.TextField(verbose_name="Tweet")
    image = models.ImageField(upload_to="tweet_images", blank=True, null=True, verbose_name="Image")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update time")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Owner")
    likes = models.ManyToManyField(User, related_name='liked_tweets')
    favorites = models.ManyToManyField(User, related_name='favorited_tweets')

    class Meta:
        db_table = "tweet"
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
        ordering = ("id",)

    def __str__(self):
        return f"Tweet №{self.id}, Owner: {self.owner}"
    
