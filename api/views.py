from rest_framework import generics

from cms.models import Page, Component
from .serializers import PageSerializer


class PageList(generics.ListCreateAPIView):
	"""
	API endpoint for listing and creating Page objects
	"""
	queryset = Page.objects.all()
	serializer_class = PageSerializer
