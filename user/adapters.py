from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.files.base import ContentFile
import requests

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        # Сначала вызываем реализацию метода по умолчанию,
        # чтобы сохранить пользователя и получить его экземпляр
        user = super().save_user(request, sociallogin, form)
        
        # Далее, если пользователь регистрируется через Google,
        # используем его адрес электронной почты без @gmail.com в качестве имени пользователя
        if sociallogin.account.provider == 'google':
            email = user.email.split('@')[0]
            user.username = email
            full_name = sociallogin.account.extra_data.get('name')
            picture = sociallogin.account.extra_data.get('picture')

            if full_name:
                user.name = full_name
                
            if picture:
                # Загрузка изображения по URL и сохранение в поле изображения пользователя
                response = requests.get(picture)
                if response.status_code == 200:
                    user.image.save(f"{user.username}_profile_picture.jpg", ContentFile(response.content), save=True)
        # Сохраняем изменения в профиле пользователя
        user.save()
        
        # Возвращаем экземпляр пользователя
        return user