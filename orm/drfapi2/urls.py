from django.urls import path
from . import views

urlpatterns = [
    path('show/',views.TeacherInfoList.as_view(),),
    # path('show_info/<int:pk>/',views.show_teacherInfo,),
    path('show_create/', views.TeacherInfoCreate.as_view()),
]
