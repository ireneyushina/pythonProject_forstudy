from django.db import models

class Buyer(models.Model):
    username = models.CharField('Имя покупателя', max_length=15),
    usernumber = models.PositiveIntegerField('Номер получателя')

    def __str__(self):
        return self.username