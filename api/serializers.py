from rest_framework import serializers

from cms.models import  Page


class PageSerializer(serializers.ModelSerializer):

	class Meta:
			model = Page
			fields = ('title', 'is_public')
