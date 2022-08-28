from django.db import models
from jsonfield import JSONField


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    offer = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    days = models.CharField(max_length=2)
    validUpto = models.CharField(max_length=10)
    ValidOffer = models.CharField(max_length=10)
    date = models.CharField(max_length=50)
    benefits = JSONField()
    overview = JSONField()

    # headerImg = models.ImageField()
    # image1 = models.ImageField()
    # image2 = models.ImageField()
    # image3 = models.ImageField()
    # image4 = models.ImageField()
    # image5 = models.ImageField()

    def __str__(self):
        return self.title
