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


class reviews(models.Model):
    username = models.CharField(max_length=25)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    comment = models.TextField(max_length=500, blank=False)


class attachment(models.Model):
    message = models.ForeignKey(reviews, verbose_name=_('reviews'), on_delete=models.CASCADE)
    file = models.FileField(_('attachment'), upload_to='gallery')