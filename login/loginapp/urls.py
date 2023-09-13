from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView
from .views import CustomPasswordChangeDoneView

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
    path('doubleac',views.doubleac, name='doubleac'),
    path('chathome', views.chathome, name='chathome'),
    path('chatroom/<str:room_name>/', views.chatroom, name='chatroom'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profele/delete/', views.profile_delete, name='profile_delete'),
    path('profile/anke/', views.profile_anke, name='profile_anke'),
    path('profile/password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/password_change_done/',  CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('board/create/', views.board_create, name='board_create'),
    path('board/list/', views.board_list, name='board_list'), 
    path('board/edit/<int:id>', views.board_edit, name='board_edit'),
    path('board/delete/<int:id>', views.board_delete, name='board_delete'),
    path('board/post_texts/<int:topic_id>', views.board_post_texts, name='board_post_texts'),
   
]