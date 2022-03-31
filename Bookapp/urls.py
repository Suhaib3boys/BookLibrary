from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewBook.as_view(),name='index'),
    path('add/', AddBook.as_view(), name='add'),
    path('detail/<int:pk>/',DetailBook.as_view(),name='detail'),
    path('update/<int:pk>/',UpdateBook.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteBook.as_view(),name='delete-book')


]
