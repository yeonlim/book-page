from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="book"),
    path('<str:id>', detail, name="book_detail"),
    path('new/', new, name="book_new"),
    path('edit/<str:id>', edit, name="book_edit"),
    path('delete/<str:id>', delete, name="book_delete"),
    path('search/', search, name="book_search"),
]