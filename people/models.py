from django.db import models


class People(models.Model):
    full_name = models.CharField(max_length=256)
    birth_date = models.DateField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
