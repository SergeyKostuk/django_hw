from django.db import models


class Album(models.Model):
    name_of_album = models.CharField(max_length=50, null=True, default=None)
    start_date = models.DateField(null=False)

    band = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='alb', )

    def __str__(self):
        return self.name_of_album


class MusicBand(models.Model):
    name = models.CharField(max_length=255, default=None)
    age = models.IntegerField()
    style = models.CharField(max_length=255, default=None)



    def __str__(self):
        return f'{self.name}{self.style}'


class Track(models.Model):
    name_of_trask = models.CharField(max_length=4, default=None)
    size = models.PositiveSmallIntegerField()
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL, related_name='track', )
    def __str__(self):
        return f'{self.name_of_trask}'

from django.db import models

# Create your models here.
# a = MusicBand.objects.filter().first()
# all_albums_of_a = a.alb.all()
#
# b = Album.objects.filter().first()
# all_tracks_of_album = b.track.all()