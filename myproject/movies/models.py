from django.db import models

# Creaclaste your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    sinopse = models.TextField()
    duration = models.IntegerField()
    release_date = models.DateField()
    cover = models.ImageField(upload_to='movies/covers')
    trailer = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Meta:
    Verbose_name = 'Filme'
    Verbose_name_plural = 'Filmes'
    ordering = ['title']