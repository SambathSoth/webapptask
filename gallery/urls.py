from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns=[
    path('', views.home, name='home'),
    path('detail1/', views.detail1, name='detail1'),
    path('detail2/', views.detail2, name='detail2'),
]
