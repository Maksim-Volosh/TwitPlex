from django.shortcuts import render

from django.http import JsonResponse
from .models import Tweets

def like_tweet(request):
    if request.method == 'POST':
        tweet_id = request.POST.get('tweet_id')
        if tweet_id:
            try:
                tweet = Tweets.objects.get(pk=tweet_id)
                user = request.user
                if user in tweet.likes.all():
                    # Если пользователь уже лайкнул твит, убираем лайк
                    tweet.likes.remove(user)
                    liked = False
                else:
                    # Если пользователь еще не лайкнул твит, добавляем лайк
                    tweet.likes.add(user)
                    liked = True
                likes_count = tweet.likes.count()
                print('Likes count:', likes_count, "id tweets:", tweet_id) # Отладочный вывод в консоль

                # Возвращаем JSON-ответ с информацией о лайке и общем количестве лайков
                return JsonResponse({'liked': liked, 'likes_count': likes_count})
            except Tweets.DoesNotExist:
                pass
    return JsonResponse({})

