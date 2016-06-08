from django.forms import ModelForm
from .models import Category, Shop, Review


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class ShopForm(ModelForm):

    class Meta:
        model = Shop
        fields = ['name', 'phone', 'address', 'explanation', 'image1', 'image2', 'image3', 'category']


class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields = ['content']
