"""health_api URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'Health Data API',
        'endpoints': {
            'health_data': '/api/health-data/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('health_data.urls')),
    path('', api_root, name='api_root'),
]
