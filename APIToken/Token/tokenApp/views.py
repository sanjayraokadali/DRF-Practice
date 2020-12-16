from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from tokenApp.models import UserList
from tokenApp.serializers import UserSerializer

# Create your views here.
class BaseView(APIView):

    def get(self,request):

        u = UserList.objects.all()

        s = UserSerializer(u, many=True)

        return Response(s.data)

    def post(self, request):


        s = UserSerializer(data = request.data)

        if s.is_valid():

            s.save()

            return Response(s.data)
