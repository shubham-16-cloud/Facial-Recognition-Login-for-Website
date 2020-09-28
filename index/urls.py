from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('info/<str:id1>',views.info,name='info'),
    
]