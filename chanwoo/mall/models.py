import os
import uuid
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "Category {}".format(self.pk)

    def get_absolute_url(self):
        return reverse("mall:category_detail", args=[self.pk])


def random_directory_path(instance, filename):
    app_label = instance.__class__._meta.app_label
    cls_name = instance.__class__.__name__.lower()
    ymd_path = timezone.now().strftime("%y/%m/%d")
    filename = ".".join([uuid.uuid4().hex, filename.rsplit(".")[-1]])
    return os.path.join(app_label, cls_name, ymd_path, filename)


class Shop(models.Model):

    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True, related_name="shops")

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=4095)
    explanation = models.TextField(max_length=65535)

    image1 = models.ImageField(upload_to=random_directory_path)
    image2 = models.ImageField(upload_to=random_directory_path, blank=True, null=True)
    image3 = models.ImageField(upload_to=random_directory_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "Shop {}".format(self.pk)

    def get_absolute_url(self):
        return reverse("mall:shop_detail", args=[self.pk])


class Review(models.Model):

    shop = models.ForeignKey(Shop, models.CASCADE, related_name="reviews")
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name="reviews")

    content = models.TextField(max_length=65535)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Review {}".format(self.pk)

    def get_absolute_url(self):
        return reverse("mall:shop_detail", args=[self.shop.pk])
