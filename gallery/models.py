from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# review models

RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )


class Reviews(models.Model):
    username = models.CharField(max_length=25, blank=False)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    title = models.CharField(max_length=50, blank=False)
    comment = models.TextField(max_length=500, blank=False)
    
    
    def __str__(self):
        return self.title

class Attachment(models.Model):
    review_table = models.ForeignKey(Reviews, related_name="attachment", on_delete=models.CASCADE)
    file = models.FileField(upload_to='gallery')
    
    def __str__(self):
        return " '{0}' is part of '{1}' ".format(self.file, self.review_table.title)