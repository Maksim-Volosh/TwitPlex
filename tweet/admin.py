from django.contrib import admin
from django.template.defaultfilters import truncatechars
from tweet.models import Tweets

class TweetsAdmin(admin.ModelAdmin):
    list_display = ['tweet_t', 'owner', 'image', 'time_create', 'likes_count', 'id']
    readonly_fields = ['likes_count']  # only read 
    
    def tweet_t(self, obj):
        return truncatechars(obj.tweet, 100) 
    
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Number of likes"

    def id(self, obj):
        return obj.id
    

    

admin.site.register(Tweets, TweetsAdmin)
