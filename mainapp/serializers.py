from dataclasses import field
from rest_framework import serializers
from mainapp.models import Company
from django.conf import settings


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for company model"""
    #start_date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    #end_date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Company
        fields = ('__all__')




