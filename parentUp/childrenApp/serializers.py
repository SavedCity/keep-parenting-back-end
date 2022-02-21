from dataclasses import fields
from rest_framework import serializers
from .models import Children

class ChildrenSerializers(serializers.ModelSerializer):
    class Meta:
        model=Children
        fields=('child_id', 'first_name', 'last_name', 'gender', 'birth_date', 'description', 'image', 'created_date', 'created_by')