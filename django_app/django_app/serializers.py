from rest_framework import serializers
from django_app.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'age', 'address', 'salary', 'join_date')
