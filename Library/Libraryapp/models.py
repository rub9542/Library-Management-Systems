from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date,timedelta
# Create your models here.


class Librarian(models.Model):
    name = models.CharField(max_length=200)
    age= models.CharField(max_length=2)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    # def get_name(self):
    #     return self.l_name


class Book(models.Model):
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    # book_price = models.IntegerField(default=0)
    # author = models.CharField( max_length=200)
    stock = models.IntegerField(default=1)
    # no_of_copies = models.IntegerField(default=1)
    isbn = models.IntegerField()

    # available_books = models.IntegerField(default=5)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=200)
    loc = models.CharField(max_length=200)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Member, on_delete=models.CASCADE)


class BookIssue(models.Model):

    issued_to = models.ForeignKey(Member, on_delete=models.CASCADE)
    # book_to_issue = models.ForeignKey('Book',null=True,on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField()
    returned_date=models.DateTimeField()
    issued_by = models.ForeignKey(Librarian,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_returned=models.BooleanField(default=False)
    # penalty=models.IntegerField(default=0)

    @property
    def fine(self):
        if self.returned_date is not None:
            time_difference = self.returned_date - self.return_date
            if time_difference.days > 0:
                return time_difference.days * 10
        else:
            return 0

    # def is_return(self):
    #     if self.returned_date is not None:
    #         self.is_returned = True
    #         return True


@receiver(post_save,sender=BookIssue)
def is_returned(sender, instance,**kwargs):
    book=instance.book
    if instance.is_returned:

        book.stock = book.stock+1

        book.save()
    else:
        if book.stock >= 0:
            book.stock = book.stock-1
        else:
            book.stock = 0
        book.save()
