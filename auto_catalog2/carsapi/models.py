from django.db import models
from django.db.models import Avg


class Car(models.Model):

    class Meta:
        db_table = 'cars'

    RATE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    make = models.CharField(max_length=25, blank=False, null=False)
    model = models.CharField(max_length=25, blank=False, null=False)
    rating = models.IntegerField(default=1, choices=RATE)

    def __str__(self):
        return self.make


avg_raitnig = Car.objects.aggregate(duration=Avg('rating'))
