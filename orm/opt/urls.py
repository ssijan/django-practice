from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('result/', views.result, name='result'),
    path('result/pdf/<str:student_id>/', views.result_pdf, name='result_pdf'),
    path('result/<str:student_id>/', views.send_result_mail, name='send_mail')
]
