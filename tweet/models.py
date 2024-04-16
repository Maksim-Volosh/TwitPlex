from django.db import models

from user.models import User

class Tweets(models.Model):
    tweet = models.TextField(verbose_name = "Tweet")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name = "Изображение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Create time")
    time_update = models.DateTimeField(auto_now=True, verbose_name = "Update time")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name = "Owner")
    
    
    class Meta:
        db_table = "tweet"
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
        ordering = ("id",)
        
    def __str__(self):
        return f"Tweet {self.id}"
    
class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "favorites"
    
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "likes"
