from rest_framework import serializers
from .models import ShortUrl
from . shorting import create_short_url


class ShortURLSerialaizer(serializers.Serializer):
    url = serializers.CharField(max_length=255)

    def create(self, validated_data):
        short = dict(short_url=create_short_url(validated_data['url']))
        validated_data.update(short)
        return ShortUrl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        instance.short_url = validated_data.get('short_url', instance.short_url)
        instance.save()
        return instance
