from django.contrib import admin
from .models import Album, Track,MusicBand

# Register your models here.
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(MusicBand)
