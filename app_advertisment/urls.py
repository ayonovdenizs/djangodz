from django.urls import path
from .views import index, advertisement_post

urlpatterns = [
    path('', index, name = 'main-page'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
]
