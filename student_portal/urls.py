from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('login/', views.Login, name='login' ),
    path('logout/', views.Logout, name='logout' ),
    path('', views.Student_portal, name='student_portal'),
    path('self_services/', views.Student_self_services, name='student_self_services'),
    path('personal_information/', views.Student_personal_information, name='student_personal_information'),
    path('online_learning/', views.Student_online_learning, name='student_online_learning'),
    path('online_payments/', views.Student_payments, name='student_payments'),
    path('result_checker/', views.Student_results, name='student_view_results'),
]
