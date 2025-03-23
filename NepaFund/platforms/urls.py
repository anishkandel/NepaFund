from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='platforms'),
    path('<int:platform_id>/',views.platform, name='platform'),
    path('search', views.search, name='search'),
]

