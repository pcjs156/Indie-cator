from django.contrib import admin
from .models import Event, Comment

admin.site.register(Comment)
admin.site.register(Event)