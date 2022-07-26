from django.contrib import admin
from django.urls import path
from dashboard import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),

    path('coBuying/', views.coBuying, name='coBuying'),
    path('delivery/', views.delivery, name='delivery'),
    path('detailView/', views.detailView, name='detailView'),
    path('signup/', accounts_views.signup, name='signup'),
    path('success/', accounts_views.success, name='success'),
    
]