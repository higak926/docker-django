from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text)

# first secret generate command↓
# python generate_secretkey_setting.py > local_settings.py
