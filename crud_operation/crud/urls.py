from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name ='index'),
    path('login/', views.login_page, name ='login_page'),
    path('logout/', views.logOut, name ='logOut'),
    path('search/', views.search_item, name='search_item'),
    path('register/', views.register_page, name ='register_page'),
    path('add_item/', views.add_item, name ='add_item'),
    path('delete-info/<int:id>/', views.delete_info, name = "delete_info"),
    path('update-info/<int:id>/', views.update_info, name = "update_info"),
]
