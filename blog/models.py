from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='images/')
    dateadded = models.DateField(auto_now=True)

    QUARANTINE = 'quarantine'
    STIGMA = 'stigma'
    TESTING = 'testing'
    CATEGORY = [
        (QUARANTINE, ('Quarantine related')),
        (STIGMA, ('Stigma related')),
        (TESTING, ('Testing related')),
        ]
    category = models.CharField(
       max_length=32,
       choices=CATEGORY,
       default=STIGMA,
       )

    def dateadded_pretty(self):
        return self.dateadded.strftime('%B %e, %Y')

    def __str__(self):
        return self.title
