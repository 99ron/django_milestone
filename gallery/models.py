from django.db import models
from django.contrib.auth.models import User
from orders.models import OrderList
from profiles.models import UserProfile
from django.utils.translation import ugettext_lazy as _

# Gallery models

# This is used for the rating option.
RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

class Reviews(models.Model):
    order_number = models.ForeignKey(OrderList, related_name="review_table", on_delete=models.DO_NOTHING)
    user_int = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    title = models.CharField(max_length=50, blank=False)
    comment = models.TextField(max_length=500, blank=False)
    review_left = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number.service_id.invoice_no

class Attachment(models.Model):
    review_table = models.ForeignKey(Reviews, related_name="attachment", on_delete=models.CASCADE)
    file = models.FileField(upload_to='gallery')
    
    def __str__(self):
        return " '{0}' is part of '{1}' ".format(self.file, self.review_table.title)