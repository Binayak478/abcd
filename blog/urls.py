from django.urls import path
from .views.auth_view import login,register
from .views.crud_view import create,edit,home,single,delete

urlpatterns = [
    path('login/',login,name="login"),#herna baki
    path('register/',register,name='register'),
    path('',home, name='home'),
    path('create/',create,name='create'),
    path('edit/',edit,name='edit'),
    path('<int:blog_id>',single,name='single'),#herna baki
    path('<int:blog_id>/delete',delete, name='delete_blog')
]
