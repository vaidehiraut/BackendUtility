from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Sample
from .serializers import SampleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework import generics
from rest_framework import mixins
import requests
import json
from rest_framework_xml.renderers import XMLRenderer
import logging

# Create your views here.


class SampleAPIView(APIView):
    def post(self, request):
        logging.basicConfig(filename='test.txt', level=logging.DEBUG)

        serializer = SampleSerializer(data=request.data)
        logging.debug(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, format=None):
        #     response = requests.get("https://api.covid19api.com/countries").json()
        #     print(response)
        #     return render(request,'home.html',{'response':response})


# Generic API views
# class MyXMLRenderer(XMLRenderer):
# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
# mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

#     serializer_class = SampleSerializer
#     queryset = Sample.objects.all()

#     lookup_field = 'id'

#     def get(self, request, id = None):

#         if id:
#             return self.retrieve(request)
#         else:
            # print(request.data)
    #         return self.list(request)

    # def post(self, request):
    #     print(request.data)
    #     return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)

    # def delete(self, request, id):
        # return self.destroy(request, id)



# Class based API views
# class SampleAPIView(APIView):
#     def get(self, request):
#         samples = Sample.objects.all()
#         serializer= SampleSerializer(samples, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SampleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class SampleDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Sample.objects.get(id=id)
#         except Sample.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         sample = self.get_object(id)
#         serializer= SampleSerializer(sample)
#         return Response(serializer.data)

#     def put(self, request, id):
#         sample = self.get_object(id)
#         serializer = SampleSerializer(sample, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, id):
#         sample = self.get_object(id)
#         sample.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Function based API views
# @api_view(['GET', 'POST'])
# def sample_list(request):
#     if request.method == 'GET':
#         samples = Sample.objects.all()
#         serializer= SampleSerializer(samples, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SampleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def sample_detail(request, pk):
#     try:
#         sample = Sample.objects.get(pk=pk)
#     except Sample.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer= SampleSerializer(sample)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SampleSerializer(sample, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         sample.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)