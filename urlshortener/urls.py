from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Shortener Urls
    path('', include('main_app.urls'))
]


