from django.urls import path
from.import views

urlpatterns=[

path('',views.index,name='index'),

path('login/',views.login,name='login'),
path('loguser/',views.loguser,name='loguser'),
path('logoutuser/',views.logoutuser,name='logoutuser'),
path('loggeduser/',views.loggeduser,name='loggeduser')


]