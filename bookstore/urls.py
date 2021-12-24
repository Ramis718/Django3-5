from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_view'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_datail_view'),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name='book_update_view'),
    path('books/<int:id>/delete/', views.BookDeleteView.as_view(), name='book_delete_view'),
    path('add-book/', views.BookCreateViev.as_view(), name='add_book_view'),
#     path('books/', views.get_books, name='book_view'),
#     path('books/<int:id>/', views.book_detail, name='book_detail_view'),
#     path('add-book/', views.add_book, name='add_book_view'),
#     path('add-comments/', views.add_comments, name='add_comments_view'),
]
