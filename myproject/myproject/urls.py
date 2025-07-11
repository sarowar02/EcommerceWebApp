"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to Testview. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function Testview
    1. Add an import:  from my_app import Testview
    2. Add a URL to urlpatterns:  path('', Testview.home, name='home')
Class-based Testview
    1. Add an import:  from other_app.Testview import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myproject import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
    path('product/',include('product.urls')),
    path('crudapp/',include('crudapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/',include('categories.urls')),

]
