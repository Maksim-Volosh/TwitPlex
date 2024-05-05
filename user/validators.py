from django.core.validators import RegexValidator
import re

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