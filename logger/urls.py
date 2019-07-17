from django.conf.urls import url
from logger import views
from django.contrib.auth import login, logout
# SET THE NAMESPACE!
app_name = 'logger'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^dash/$', views.dash, name='dash'),
]