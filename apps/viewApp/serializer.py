from rest_framework import serializers

from apps.viewApp.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', 'id']
