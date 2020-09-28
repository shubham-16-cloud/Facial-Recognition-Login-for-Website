from django.urls import path
from . import views
urlpatterns = [
    path('sign-up',views.signup, name='signup'),
    path('login1', views.login1, name='login1'),
    path('logout', views.logout1, name='logout'),
    path('creat_user',views.creat_user, name='creat_user'),
    path('detect',views.detectface, name= 'detectface'),
    path('home/<int:id>',views.home,name= 'home')
]