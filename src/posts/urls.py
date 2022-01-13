from django.urls import path
from .views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = 'posts'
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('<slug:slug>', BlogPostDetail.as_view(), name="detail"),
    path("create/", BlogPostCreate.as_view(), name='create'),
    path('edit/<slug:slug>', BlogPostUpdate.as_view(), name="edit"),
    path('delete/<slug:slug>', BlogPostDelete.as_view(), name="delete"),

]
