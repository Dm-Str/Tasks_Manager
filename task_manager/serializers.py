from rest_framework import serializers
from task_manager.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        def validate_title(self, value):
            if not value:
                raise serializers.ValidationError("Поле title не может быть пустым.")
            return value
