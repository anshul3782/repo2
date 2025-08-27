from rest_framework import serializers
from .models import HealthData

class HealthDataSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    
    class Meta:
        model = HealthData
        fields = ['phone_number', 'username', 'steps', 'avg_heart_rate', 'resting_calories', 'sleep_hours', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_phone_number(self, value):
        """Validate phone number format"""
        if not value.isdigit():
            raise serializers.ValidationError("Phone number should contain only digits.")
        if len(value) < 10:
            raise serializers.ValidationError("Phone number should be at least 10 digits.")
        return value

    def validate_steps(self, value):
        """Validate steps count"""
        if value < 0:
            raise serializers.ValidationError("Steps cannot be negative.")
        if value > 100000:
            raise serializers.ValidationError("Steps count seems unrealistic.")
        return value

    def validate_avg_heart_rate(self, value):
        """Validate heart rate"""
        if value < 0:
            raise serializers.ValidationError("Heart rate cannot be negative.")
        if value > 300:
            raise serializers.ValidationError("Heart rate seems unrealistic.")
        return value

    def validate_resting_calories(self, value):
        """Validate resting calories"""
        if value < 0:
            raise serializers.ValidationError("Resting calories cannot be negative.")
        return value

    def validate_sleep_hours(self, value):
        """Validate sleep hours"""
        if value < 0:
            raise serializers.ValidationError("Sleep hours cannot be negative.")
        if value > 24:
            raise serializers.ValidationError("Sleep hours cannot exceed 24.")
        return value
