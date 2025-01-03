from django.urls import path
from . import views

urlpatterns = [


    path('sign_in_admin', views.sign_in_admin , name='sign_in_admin'),

    path('signup_patient', views.signup_patient, name="signup_patient"),
    path('sign_in_patient', views.sign_in_patient , name='sign_in_patient'),
    path('savepdata/<str:patientusername>', views.savepdata , name='savepdata'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('password_reset_success/', views.password_reset_success, name='password_reset_success'),

    path('signup_doctor', views.signup_doctor , name="signup_doctor"),
    path('sign_in_doctor', views.sign_in_doctor , name='sign_in_doctor'),
    path('saveddata/<str:doctorusername>', views.saveddata , name='saveddata'),
    path('forgot_passwordd',views.forgot_passwordd,name='forgot_passwordd'),
    path('password_success',views.password_success,name='password_success'),

    path('logout', views.logout , name='logout'),
]