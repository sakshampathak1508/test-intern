from rest_framework import serializers
from.models import Restaurant,Hour

class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model= Restaurant
        field = '__all__'