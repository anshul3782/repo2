from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import HealthData
from .serializers import HealthDataSerializer

class HealthDataViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing health data instances.
    
    Provides:
    - GET /api/health-data/ - List all health data
    - POST /api/health-data/ - Create new health data
    - GET /api/health-data/{phone_number}/ - Get specific user's data
    - PUT /api/health-data/{phone_number}/ - Update user's data
    - PATCH /api/health-data/{phone_number}/ - Partial update user's data
    - DELETE /api/health-data/{phone_number}/ - Delete user's data
    """
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    lookup_field = 'phone_number'

    def list(self, request, *args, **kwargs):
        """List all health data with pagination"""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': queryset.count(),
            'results': serializer.data
        })

    def create(self, request, *args, **kwargs):
        """Create new health data entry"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Health data created successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def retrieve(self, request, *args, **kwargs):
        """Get health data for specific phone number"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'message': 'Health data retrieved successfully',
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        """Update health data for specific phone number"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response({
            'message': 'Health data updated successfully',
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        """Delete health data for specific phone number"""
        instance = self.get_object()
        phone_number = instance.phone_number
        self.perform_destroy(instance)
        return Response({
            'message': f'Health data for {phone_number} deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get overall statistics of health data"""
        from django.db.models import Avg, Max, Min, Count
        
        stats = HealthData.objects.aggregate(
            total_users=Count('phone_number'),
            avg_steps=Avg('steps'),
            avg_heart_rate=Avg('avg_heart_rate'),
            avg_sleep_hours=Avg('sleep_hours'),
            max_steps=Max('steps'),
            min_steps=Min('steps'),
        )
        
        return Response({
            'message': 'Health data statistics',
            'stats': stats
        })

    @action(detail=True, methods=['patch'])
    def update_steps(self, request, phone_number=None):
        """Update only steps for a specific user"""
        instance = self.get_object()
        steps = request.data.get('steps')
        
        if steps is None:
            return Response(
                {'error': 'Steps value is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            instance.steps = int(steps)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response({
                'message': 'Steps updated successfully',
                'data': serializer.data
            })
        except (ValueError, TypeError):
            return Response(
                {'error': 'Invalid steps value'},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=['patch'])
    def update_heart_rate(self, request, phone_number=None):
        """Update only heart rate for a specific user"""
        instance = self.get_object()
        heart_rate = request.data.get('avg_heart_rate')
        
        if heart_rate is None:
            return Response(
                {'error': 'Heart rate value is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            instance.avg_heart_rate = int(heart_rate)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response({
                'message': 'Heart rate updated successfully',
                'data': serializer.data
            })
        except (ValueError, TypeError):
            return Response(
                {'error': 'Invalid heart rate value'},
                status=status.HTTP_400_BAD_REQUEST
            )
