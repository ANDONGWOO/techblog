from django.urls import path
from . import views

app_name = "app1"#앱이름

urlpatterns = [
    #app1/ 기본 
    path('', views.index, name='index'),
    path('<int:pk>/',views.detail, name='detail'),
    
]
