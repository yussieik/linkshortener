from django.urls import path

from .views import home_view, redirect_url_view

appname = "shortener"

urlpatterns = [
    path('create', home_view, name='home'),
    path('s/<str:shortened_part>', redirect_url_view, name='redirect'),
]
