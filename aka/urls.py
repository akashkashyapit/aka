from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='home'),
    path('contact/',views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('count/',views.count, name='count'),
]
