from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "Category {}".format(self.pk)

    def get_absolute_url(self):
        return reverse("mall:category_detail", args=[self.pk])


class Shop(models.Model):

    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True, related_name="shops")

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=4095)
    explanation = models.TextField(max_length=65535)

    image1 = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)

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
