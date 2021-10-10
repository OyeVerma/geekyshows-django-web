
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('get/', views.get_data_from_database),
    path('search/', views.search, name='search'),
    path('save/', views.save),
    path('success/', views.success),
    path('form/', views.form),
    path("user/", views.user, name="user_registration"),
    path('project/<int:u>/<int:theta>/', views.views.proj_u_theta),
    
]
