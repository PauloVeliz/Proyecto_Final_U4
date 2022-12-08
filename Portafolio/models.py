from django.db import models

# Create your models here.

class Proyecto(models.Model):
    foto = models.URLField()
    titulo_proyecto = models.TextField()
    desc_proyecto = models.TextField()
    tags = models.TextField()
    url_github = models.URLField()
