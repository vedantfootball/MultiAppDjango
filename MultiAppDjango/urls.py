from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1_views.home, name='home'),
    path('app2/', app2_views.sample_page, name='sample_page'),
]
