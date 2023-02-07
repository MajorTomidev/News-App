from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializers import NewsSerializer
from blog.models import News

# Create your views here.
@api_view(['GET'])
def api_list_page(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response (serializer.data, status=status.HTTP_200_OK)

class Api_list_page(APIView):
     def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response (serializer.data)
     
@api_view(['GET'])
def api_detail_page(request, slug):
    if request.method == 'GET':
        news = News.objects.get(slug=slug)
        serializer = NewsSerializer(news, many=True)
        return Response (serializer.data)
    
class Api_detail_page(APIView):
    def get(self, request, slug):
        news = News.objects.get(slug=slug)
        serializer = NewsSerializer(news)
        return Response (serializer.data)
    
@api_view(['POST'])
def api_create_page(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class api_create_class_page(APIView):
    def get(self, request):
       serializer = NewsSerializer(data=request.data)
       if serializer.is_valid():
        serializer.save()
        return Response (serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def api_update_page(request, slug):
    try:
        news = News.objects.get(slug=slug)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = NewsSerializer(news, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    


    
