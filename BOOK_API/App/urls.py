from django.urls import path
from App.views import *

urlpatterns = [

    path('addbook/',ViewBooks),
    path('genericbook',GenericBook.as_view()),
    path('bookclass/',BookClass.as_view())
]
