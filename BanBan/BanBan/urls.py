from django.contrib import admin
from django.urls import path
from dashboard import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    #path('login/', accounts_views.login, name='login'),
    #path('logout/', accounts_views.logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    path('coBuying/', views.coBuying, name='coBuying'),
    path('delivery/', views.delivery, name='delivery'),
    path('detailView/', views.detailView, name='detailView'),
    path('signup/', accounts_views.signup, name='signup'),
    path('success/', accounts_views.success, name='success'),
    
]