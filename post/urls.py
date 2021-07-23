from django.urls import path
from .views import create_post, home_view,post_detail_view

urlpatterns = [
    path('Add_post/',create_post, name='Add Post'),
    path('', home_view, name='home'),
    path('post_detail/<int:id>', post_detail_view, name='detail_post'),
]