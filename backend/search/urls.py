from django.urls import path

from . import views

urlpatterns = [
    path('', views.SerachListView.as_view(), name='search')
]