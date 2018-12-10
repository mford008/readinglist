from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status_choices = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    )
    status = models.CharField(choices=status_choices, default='new')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title, self.author
