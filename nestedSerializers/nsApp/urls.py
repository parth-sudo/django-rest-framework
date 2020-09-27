from django.urls import path, include
from nsApp import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='List'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='Detail'),

    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>', views.BookDetailView.as_view()),

]
