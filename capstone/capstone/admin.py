from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Playlist)
admin.site.register(Playinglist)
admin.site.register(Playedlist)