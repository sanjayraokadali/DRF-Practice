from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from App.models import AddBook
from App.serializers import BookSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

class GenericBook(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin):

    serializer_class = BookSerializer

    queryset = AddBook.objects.all()

    def get(self,request):

        return self.list(request)

    def post(self,request):

        return self.create(request)

    def put(self,request, id=None):

        return self.update(request, id)



class BookClass(APIView):

    def get(self,request):

        books = AddBook.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self,request):

        content = BookSerializer(data = request.data)

        if content.is_valid():
            content.save()
            books = AddBook.objects.all()
            serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

@api_view(['GET','POST'])
def base(request):

    return Response('Welcome')


@api_view(['GET','POST'])
def ViewBooks(request):

    if request.method == 'GET':

        books = AddBook.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':


        content = BookSerializer(data = request.data)

        if content.is_valid():
            content.save()
            books = AddBook.objects.all()
            serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
