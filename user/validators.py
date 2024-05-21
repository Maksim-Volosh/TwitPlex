from django.core.validators import RegexValidator
import re

from django.forms import ValidationError
from django.utils import timezone

latin_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9_]+$',
    message='Username can only contain Latin letters, numbers and underscores.',
    code='invalid_input'
    )

password_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9!@#$%^&*()-_+=]+$',
    message='Password can only contain Latin letters, numbers, and special characters.',
    code='invalid_input'
)

def username_change_limit_validator(user, new_username):
    last_change_date = user.last_change_date
    
    if last_change_date:
        days_since_change = (timezone.now() - last_change_date).days
        days_left = 14 - days_since_change
        
        old_username = user.username
        if days_since_change < 14 and new_username != old_username:
            raise ValidationError(f"You can change your username after {days_left} days.")