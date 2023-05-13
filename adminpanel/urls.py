from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('adminpanel',views.adminlogin),
    path('admin_homepage',views.admin_homepage),
    path('user_edit',views.user_edit),
    path('user_block',views.user_block),
    path('user_delete',views.user_delete),
    path('user_update',views.user_update),
    path('user_add',views.user_add),
    path('admin_logout',views.admin_logout),
    path('searched',views.searched, name="searched")
    

]