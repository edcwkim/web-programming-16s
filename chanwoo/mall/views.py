from django.views import generic
from .models import Category, Shop, Review


class Index(generic.ListView):

    model = Category
    context_object_name = "categories"
    template_name = "mall/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.order_by('-created_at').all()
        return context


class CategoryDetail(generic.DetailView):

    model = Category
    context_object_name = "category"
    template_name = "mall/category_detail.html"


class CategoryCreate(generic.CreateView):

    pass


class CategoryUpdate(generic.UpdateView):

    pass


class ShopDetail(generic.DetailView):

    model = Shop
    context_object_name = "shop"
    template_name = "mall/shop_detail.html"


class ShopCreate(generic.CreateView):

    pass


class ShopUpdate(generic.UpdateView):

    pass


class ReviewCreate(generic.CreateView):

    pass


class ReviewUpdate(generic.UpdateView):

    pass
