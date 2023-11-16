from rest_framework import serializers
from ..models import CourseTerm


class CourseTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTerm
        fields = '__all__'
