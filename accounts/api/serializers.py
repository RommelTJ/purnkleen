from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework import serializers

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'url',
        ]

    def get_url(self, obj):
        return reverse_lazy("profiles:detail", kwargs={"username": obj.username})
