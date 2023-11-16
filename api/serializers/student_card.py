from rest_framework import serializers
from ..models import StudentCard


class StudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCard
        fields = '__all__'
