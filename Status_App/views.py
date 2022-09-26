from .models import *
from .serializers import *
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, parsers

class StatusListCreateApiView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class StatusRetriveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    lookup_field = 'id'