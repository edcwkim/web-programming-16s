from django.shortcuts import get_object_or_404
from django.views import generic
from .forms import CategoryForm, ShopForm, ReviewForm
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

    model = Category
    form_class = CategoryForm
    template_name = "mall/category_create.html"


class CategoryUpdate(generic.UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = "mall/category_update.html"


class ShopDetail(generic.DetailView):

    model = Shop
    context_object_name = "shop"
    template_name = "mall/shop_detail.html"


class ShopCreate(generic.CreateView):

    model = Shop
    form_class = ShopForm
    template_name = "mall/shop_create.html"


class ShopUpdate(generic.UpdateView):

    model = Shop
    form_class = ShopForm
    template_name = "mall/shop_update.html"


class ReviewCreate(generic.CreateView):

    model = Review
    form_class = ReviewForm
    template_name = "mall/review_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.shop = get_object_or_404(Shop, pk=self.args[0])
        return super().form_valid(form)


class ReviewUpdate(generic.UpdateView):

    model = Review
    form_class = ReviewForm
    template_name = "mall/review_update.html"
