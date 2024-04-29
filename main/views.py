from audioop import reverse
from datetime import datetime
from django.db.models import Count
from django.shortcuts import redirect, render

from tweet.models import Tweets

def index(request):
    if not request.session.get('second_enter', False):
        request.session['second_enter'] = True
        return redirect('welcome:index')
    else:
        tweets = Tweets.objects.annotate(
            likes_count=Count('likes'),
            favorites_count=Count('favorites')
        )
        
        tweets_flag = tweets.exists()
        
        current_year = datetime.now().year
        
        context = {
            "tweets": tweets,
            'current_year': current_year,
            "tweets_flag": tweets_flag,
        }
        return render(request, 'main/index.html', context=context)
    

