from django.urls import path
from . import views

urlpatterns = [
    path("",views.post_page,name='all_posts'),
]