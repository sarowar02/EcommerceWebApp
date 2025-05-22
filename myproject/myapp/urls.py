from django.urls  import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('path2', test.dataRender, name='path2'),
    path('htmlpage',views.htmlpage,name='html_page')
]