from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='images/')
    dateadded = models.DateField(auto_now=True)

    CATEGORY = (
        ('QUARANTINE', 'Quarantine related'),
        ('STIGMA', 'Stigma related'),
        ('TESTING', 'Testing related'),
    )
    category = models.CharField(
       max_length=32,
       choices=CATEGORY,
       default='STIGMA',
       )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-dateadded']

    def dateadded_pretty(self):
        return self.dateadded.strftime('%B %e, %Y')

    def __str__(self):
        return self.title
