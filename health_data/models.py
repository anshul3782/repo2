from django.db import models

class HealthData(models.Model):
    phone_number = models.CharField(max_length=20, primary_key=True, help_text="User's phone number")
    steps = models.IntegerField(default=0, help_text="Daily steps count")
    avg_heart_rate = models.IntegerField(default=0, help_text="Average heart rate")
    resting_calories = models.IntegerField(default=0, help_text="Resting calories burned")
    sleep_hours = models.IntegerField(default=0, help_text="Hours of sleep")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'health_data'  # This will use the existing table name
        verbose_name = 'Health Data'
        verbose_name_plural = 'Health Data'

    def __str__(self):
        return f"Health data for {self.phone_number}"

    @property
    def username(self):
        """Generate a username from phone number for API responses"""
        return f"user_{self.phone_number[-4:]}"
