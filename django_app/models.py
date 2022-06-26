from django.db import models

# Create your models here.
class Words(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    word = models.TextField()
    def __str__(self):
        return self.word

class Admins(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    telegram_id = models.BigIntegerField()
    def __str__(self):
        return f'{self.telegram_id}'

class Users(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    telegram_id = models.BigIntegerField()
    full_name = models.TextField()
    sana = models.DateTimeField(auto_now=True)
    kanal = models.TextField()
    xabar = models.TextField()
    soz = models.TextField()

