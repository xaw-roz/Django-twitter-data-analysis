from django.urls import path

from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='dashboard'),
    path('search', views.start_search, name='search'),
]