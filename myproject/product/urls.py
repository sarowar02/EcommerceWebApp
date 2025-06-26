from django.urls  import path

from . import views

urlpatterns = [
    path('home2',views.home2,name='html_page'),
    path('',views.index,name='index_page')
]