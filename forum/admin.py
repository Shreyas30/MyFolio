from django.contrib import admin

# Register your models here.
from .models import SubscribedUser,Posts

admin.site.register(SubscribedUser)
admin.site.register(Posts)