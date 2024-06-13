import django_setup
from lesson.models import *
user = User.objects.filter(email="example.com").first()
user.delete()
print(user)
