
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Admission_portal, name='admission_portal'),
    path('apply/', views.Apply, name='apply'),
    path('online_application_documents/', views.Admission_documents, name='admission_documents'),
    path('online_application_review/', views.Online_application_review, name='online_application_review'),
    path('Online_application_review_edit/<int:pk>', views.Online_application_review_edit, name='online_application_review_edit'),
    path('online_application/', views.Online_application, name='online_application'),
    path('Admission_Login/', views.Admission_Login, name='admission_login'),
    path('admissiong_logout/', views.Admission_logout, name='admission_logout'),
    path('create_account/', views.Admission_register, name='admission_register'),
]
