from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^category/new/$', views.CategoryCreate.as_view(), name="category_create"),
    url(r'^category/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name="category_detail"),
    url(r'^category/(?P<pk>\d+)/edit/$', views.CategoryUpdate.as_view(), name="category_update"),
    url(r'^category/(?P<pk>\d+)/delete/$', views.CategoryDelete.as_view(), name="category_delete"),
    url(r'^shop/new/$', views.ShopCreate.as_view(), name="shop_create"),
    url(r'^shop/(?P<pk>\d+)/$', views.ShopDetail.as_view(), name="shop_detail"),
    url(r'^shop/(?P<pk>\d+)/edit/$', views.ShopUpdate.as_view(), name="shop_update"),
    url(r'^shop/(?P<pk>\d+)/delete/$', views.ShopDelete.as_view(), name="shop_delete"),
    url(r'^shop/(\d+)/review/$', views.ReviewCreate.as_view(), name="review_create"),
    url(r'^review/(?P<pk>\d+)/edit/$', views.ReviewUpdate.as_view(), name="review_update"),
    url(r'^review/(?P<pk>\d+)/delete/$', views.ReviewDelete.as_view(), name="review_delete"),
]
