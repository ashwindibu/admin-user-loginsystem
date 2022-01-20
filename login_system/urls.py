from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_login, name='user_login' ),
    path('user_signup',views.user_signup, name='user_signup'),
    path('homepage',views.homepage),
    path('user_login',views.user_login),
    path('user_logout',views.user_logout)
    # path('formlogin',views.formlogin),
]