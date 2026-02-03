from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name ='index'),
    path('delete-info/<int:id>/', views.delete_info, name = "delete_info"),
    path('update-info/<int:id>/', views.update_info, name = "update_info")
]
