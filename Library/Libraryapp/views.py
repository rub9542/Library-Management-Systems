from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Librarian,Library,Member,Book,BookIssue
from .serializers import *
# Create your views here.


@api_view(['GET','POST'])
def api_library_view(request):
    library=Library.objects.all()
    if request.method=='GET':
        serializer=LibrarySerializer(library,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=LibrarySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)     

@api_view(['GET','POST'])
def api_book_view(request):
    book=Book.objects.all()
    if request.method=='GET':
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)     

@api_view(['GET','POST'])
def api_librarian_view(request):
    librarian=Librarian.objects.all()
    if request.method=='GET':
        serializer=LibrarianSerializer(librarian,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=LibrarianSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)     

@api_view(['GET','POST'])
def api_bookIssue_view(request):
    bookIssue=BookIssue.objects.all()
    if request.method=='GET':
        serializer=BookIssueSerializer(bookIssue,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=BookIssueSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)     


@api_view(['GET','POST']) 
def api_member_view(request):
    member=Member.objects.all()
    if request.method=='GET':
        serializer=MemberSerializer(member,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_404_NOT_FOUND)    



