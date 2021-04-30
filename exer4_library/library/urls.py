from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addAuthor/', views.addAuthor, name="addAuthor"),
    path('addBook/', views.addBook, name="addBook"),
    path('updateAuthor/<str:pk>', views.updateAuthor, name="updateAuthor"),
    path('updateBook/<str:pk>', views.updateBook, name="updateBook"),
    path('deleteAuthor/<str:pk>', views.deleteAuthor, name="deleteAuthor"),
    path('deleteBook/<str:pk>', views.deleteBook, name="deleteBook")
]
