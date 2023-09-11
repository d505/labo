from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("<str:faculty>_<str:department>",views.facaluty_department,name="facaluty_department"),
    path("detail",views.detail,name='detail'),
    path('review',views.ReviewLabolatory.as_view(), name='review'),
    path('logno',views.logno, name='logno'),
    path('noreview',views.noreview, name='noreview'),
    path('doubleac',views.doubleac, name='doubleac')
   
]