from django.db import models

class hotelusers(models.Model):
    username = models.CharField(max_length=50, default='',null=True)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username
