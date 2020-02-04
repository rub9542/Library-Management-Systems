from rest_framework import routers
from Libraryapp import views
from Libraryapp.views import *
from django.urls import path,include,re_path


urlpatterns=[
    path('library/',api_library_view,name='library-objects'),
    path('member/', api_member_view,name='member-objects'),
    path('book/', api_book_view,name='book-objects'),
    path('bookIssue/', api_bookIssue_view,name='bookissue-objects'),
    path('librarian/', api_librarian_view,name='librarian-objects')
]