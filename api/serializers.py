from rest_framework import serializers

from cms.models import Page, Component


class ComponentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Component
        fields = ('grid', 'content', 'active_image', 'initial_image')

class PageSerializer(serializers.HyperlinkedModelSerializer):
    content = ComponentSerializer(many=True, source='pages')

    class Meta:
        model = Page
        fields = ('title', 'content', )
