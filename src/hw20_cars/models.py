from django.db import models


class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return self.address


class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    weight = models.IntegerField()
    owner_full_name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    contact_info = models.OneToOneField(
        ContactInfo, null=True,
        related_name='person',
        on_delete=models.SET_NULL,
    )

    # Create your models here.
    def __str__(self):
        return self.brand
