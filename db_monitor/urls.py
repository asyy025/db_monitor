
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth',views.obtain_auth_token),
    path('system/',include('system.urls',namespace='system')),
    path('assets/', include('assets.urls',namespace='assets')),
    path('oracle/', include('oracle.urls', namespace='oracle')),
    path('mysql/', include('mysql.urls', namespace='mysql')),
    path('rds/', include('rds.urls', namespace='rds')),
    path('linux/', include('linux.urls', namespace='linux')),
]
