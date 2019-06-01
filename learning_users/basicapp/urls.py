from django.urls import path
from basicapp import views


#template URLs

app_name = 'basicapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
