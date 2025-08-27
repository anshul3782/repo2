from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'health-data', views.HealthDataViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

"""
Available endpoints:
- GET /api/health-data/ - List all health data entries
- POST /api/health-data/ - Create new health data entry
- GET /api/health-data/{phone_number}/ - Get specific user's data
- PUT /api/health-data/{phone_number}/ - Update user's data completely
- PATCH /api/health-data/{phone_number}/ - Partially update user's data
- DELETE /api/health-data/{phone_number}/ - Delete user's data

Custom endpoints:
- GET /api/health-data/stats/ - Get overall statistics
- PATCH /api/health-data/{phone_number}/update_steps/ - Update only steps
- PATCH /api/health-data/{phone_number}/update_heart_rate/ - Update only heart rate
"""
