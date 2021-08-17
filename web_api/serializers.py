from rest_framework import serializers
from .models import Userprofile , Trial

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'

class TrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trial
        fields = '__all__'