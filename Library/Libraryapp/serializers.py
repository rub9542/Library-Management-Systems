from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('available','name','stock','isbn')

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=('name','age','phone')        

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=('name','phone') 

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Library
        fields=('name','loc','librarian')

class BookIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookIssue
        fields=('issued_to','issue_date','return_date','returned_date','issued_by','book','is_returned')                       