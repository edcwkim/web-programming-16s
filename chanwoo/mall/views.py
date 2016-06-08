from django.contrib import messages
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

    def form_valid(self, form):
        messages.success(self.request, "분류 생성 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "분류 생성 실패")
        return super().form_invalid(form)


class CategoryUpdate(generic.UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = "mall/category_update.html"

    def form_valid(self, form):
        messages.success(self.request, "분류 수정 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "분류 수정 실패")
        return super().form_invalid(form)


class ShopDetail(generic.DetailView):

    model = Shop
    context_object_name = "shop"
    template_name = "mall/shop_detail.html"


class ShopCreate(generic.CreateView):

    model = Shop
    form_class = ShopForm
    template_name = "mall/shop_create.html"

    def form_valid(self, form):
        messages.success(self.request, "매장 등록 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "매장 등록 실패")
        return super().form_invalid(form)


class ShopUpdate(generic.UpdateView):

    model = Shop
    form_class = ShopForm
    template_name = "mall/shop_update.html"

    def form_valid(self, form):
        messages.success(self.request, "매장 수정 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "매장 수정 실패")
        return super().form_invalid(form)


class ReviewCreate(generic.CreateView):

    model = Review
    form_class = ReviewForm
    template_name = "mall/review_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.shop = get_object_or_404(Shop, pk=self.args[0])
        messages.success(self.request, "후기 등록 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "후기 등록 실패")
        return super().form_invalid(form)


class ReviewUpdate(generic.UpdateView):

    model = Review
    form_class = ReviewForm
    template_name = "mall/review_update.html"

    def form_valid(self, form):
        messages.success(self.request, "후기 수정 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "후기 수정 실패")
        return super().form_invalid(form)
