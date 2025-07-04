from django.urls import path
from . import views, sessionView
from django.urls import path
from .api_views import CustomLoginView, ProtectedView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('get_session/',sessionView.get_session,name='get_session'),
    path('set_session/',sessionView.set_session,name='set_session'),
    path('delete_key/',sessionView.delete_key,name='delete_key'),
    path('visit_count/',sessionView.visit_counter,name='visit_count'),
]


urlpatterns += [
    path('api/token/', CustomLoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedView.as_view(), name='token_protected'),

]