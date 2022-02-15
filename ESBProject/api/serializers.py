from dataclasses import field
from rest_framework import serializers
from .models import Sample


# class SampleSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Sample.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.save()
    #     return instance 

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        # fields = ['id','title', 'email']
        fields = '__all__'       