from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, resolve_url
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


class CategoryCreate(UserPassesTestMixin, generic.CreateView):

    model = Category
    form_class = CategoryForm
    template_name = "mall/category_create.html"

    def test_func(self):
        return self.request.user.is_superuser()

    def form_valid(self, form):
        messages.success(self.request, "분류 생성 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "분류 생성 실패")
        return super().form_invalid(form)


class CategoryUpdate(UserPassesTestMixin, generic.UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = "mall/category_update.html"

    def test_func(self):
        return self.request.user.is_superuser()

    def form_valid(self, form):
        messages.success(self.request, "분류 수정 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "분류 수정 실패")
        return super().form_invalid(form)


class CategoryDelete(UserPassesTestMixin, generic.DeleteView):

    model = Category
    template_name = "mall/delete.html"

    def test_func(self):
        return self.request.user.is_superuser()

    def get_success_url(self):
        messages.success(self.request, "분류 삭제 성공")
        return resolve_url("mall:index")


class ShopDetail(generic.DetailView):

    model = Shop
    context_object_name = "shop"
    template_name = "mall/shop_detail.html"


class ShopCreate(LoginRequiredMixin, generic.CreateView):

    model = Shop
    form_class = ShopForm
    template_name = "mall/shop_create.html"


class ShopUpdate(LoginRequiredMixin, generic.UpdateView):

    model = Shop
    form_class = ShopForm
    template_name = "mall/shop_update.html"

    def form_valid(self, form):
        messages.success(self.request, "매장 수정 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "매장 수정 실패")
        return super().form_invalid(form)


class ShopDelete(LoginRequiredMixin, generic.DeleteView):

    model = Shop
    template_name = "mall/delete.html"

    def get_success_url(self):
        messages.success(self.request, "매장 삭제 성공")
        return resolve_url("mall:index")


class ReviewCreate(LoginRequiredMixin, generic.CreateView):

    model = Review
    form_class = ReviewForm
    template_name = "mall/review_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.shop = get_object_or_404(Shop, pk=self.args[0])
        self.object.user = self.request.user
        messages.success(self.request, "후기 등록 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "후기 등록 실패")
        return super().form_invalid(form)


class ReviewUpdate(UserPassesTestMixin, generic.UpdateView):

    model = Review
    form_class = ReviewForm
    template_name = "mall/review_update.html"

    def test_func(self):
        return (self.request.user == self.get_object().user or
                self.request.user.is_superuser())

    def form_valid(self, form):
        messages.success(self.request, "후기 수정 성공")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "후기 수정 실패")
        return super().form_invalid(form)


class ReviewDelete(UserPassesTestMixin, generic.DeleteView):

    model = Review
    template_name = "mall/delete.html"
    parent = None

    def test_func(self):
        return (self.request.user == self.get_object().user or
                self.request.user.is_superuser())

    def post(self, request, *args, **kwargs):
        self.parent = self.get_object().shop
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "후기 삭제 성공")
        return resolve_url(self.parent)
