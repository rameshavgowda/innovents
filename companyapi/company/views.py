from django.shortcuts import render
from .models import company
from .serializers import companyserializer, companyserializer1
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from . pagination import MypagePagination

class Create_company(CreateAPIView):
    queryset=company.objects.all()
    serializer_class=companyserializer

class Update_company(RetrieveUpdateAPIView):
    queryset=company.objects.all()
    serializer_class=companyserializer1

class Destroy_company(RetrieveDestroyAPIView):
    queryset=company.objects.all()
    serializer_class=companyserializer

class List_company(ListAPIView):
    queryset=company.objects.all()
    serializer_class=companyserializer
    pagination_class = MypagePagination

class Retrieve_company(RetrieveAPIView):
    queryset=company.objects.all()
    serializer_class=companyserializer


