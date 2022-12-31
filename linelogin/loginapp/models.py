from django.db import models

# Create your models here.
class bform(models.Model):
    form_pk = models.CharField(max_length=100000000,primary_key=True)
    lineuid = models.CharField(max_length=50)
    name = models.CharField(max_length=20, blank=False)
    nickname = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=10, blank=False)
    email = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=50, blank=False)
    def _str_(self):
        return self.form_pk