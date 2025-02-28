from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('admdet/',views.admdet,name='admdet'),
    path('updadm/',views.updadm,name='updadm'),
    path('addadm/',views.addadm,name='addadm'),
    path('updstu<int:id>',views.updstu,name='updstu'),
    path('delstu<int:id>',views.delstu,name='delstu'),
    path('studentsession',views.studentsession,name='studentsession'),
    path('logout',views.logout,name='logout'),
    path('row',views.row,name='body'),
    path('body',views.body,name='body'),
]
