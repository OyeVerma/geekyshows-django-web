from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_show, name='add_show'),
    path('del/<int:id>', views.delete, name='delete')
]
