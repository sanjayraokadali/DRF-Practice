from rest_framework import serializers
from App.models import AddBook

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = AddBook

        fields = ('__all__')
