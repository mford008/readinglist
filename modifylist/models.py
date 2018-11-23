from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.DateField(blank=False)
    summary = models.TextField(blank=False)

    def __str__(self):
        return self.title, self.author, self.year, self.summary
