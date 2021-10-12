from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('del/<int:id>/', views.delete, name='delete'),
    path('show/<int:id>/', views.show_pass, name='show_pass'),
    path('update/<int:id>/', views.update, name='update')
]
