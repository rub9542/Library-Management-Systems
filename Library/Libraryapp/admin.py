from django.contrib import admin
from .models import Librarian,Library,Book,Member,BookIssue
from django import forms
# Register your models here.

class LibrarianAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(LibrarianAdminForm,self).__init__(*args,**kwargs)
    def clean(self):
        name=self.cleaned_data.get('name')
        if len(name)<4:
            raise forms.ValidationError('name should not be less than 4', code='error')
        return self.cleaned_data


    def save(self, commit=True):
        return super(LibrarianAdminForm, self).save(commit=commit)

class LibraryAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(LibraryAdminForm,self).__init__(*args,*kwargs)

    def clean(self):
        name=self.cleaned_data.get('name')
        if len(name)<4:
            raise forms.ValidationError('name should not be less than 4',code='error')
        return self.cleaned_data


    def save(self, commit=True):
        return super(LibraryAdminForm,self).save(commit=commit)

class BookAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name=self.cleaned_data.get('name')
        if len(name)<4:
            raise  forms.ValidationError('name should be more than 4',code='error')
        return self.cleaned_data

    def  save(self, commit=True):
        return super(BookAdminForm,self).save(commit=commit)

class  MemberAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(MemberAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        name=self.cleaned_data.get('name')
        if len(name)<4:
            raise forms.ValidationError('name should not be less than 4',code='error')
        return self.cleaned_data

    def save(self,commit=True):
        return super(MemberAdminForm,self).save(commit=commit)

# class BookIssueAdminForm(forms.ModelForm):
#     def __init__(self,*args,**kwargs):
#         super(BookIssueAdminForm,self).__init__(*args,**kwargs)
#         # if not self.instance.id:
#         #     self.fields['is_returned'].disabled = True



#     def save(self,*args,**kwargs):
#         return super(BookIssueAdminForm,self).save(commit=commit)



class LibrarianAdmin(admin.ModelAdmin) :
    list_display = ('name',)
    forms=LibrarianAdminForm

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name','librarian','loc',)
    forms=LibraryAdminForm

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','available', 'stock' ,'isbn']
    search_fields = ('name', 'stock', 'isbn',)
    forms=BookAdminForm

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','phone',)
    search_fields = ('name',)
    forms=MemberAdminForm

class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('issued_to','issue_date','return_date','returned_date','issued_by','book','is_returned', 'fine',)
    search_fields = ('book','is_returned','issued_to',)
    # forms=BookIssueAdminForm

admin.site.register(Library,LibraryAdmin)

admin.site.register(Librarian,LibrarianAdmin)

admin.site.register(Member,MemberAdmin)

admin.site.register(Book,BookAdmin)

admin.site.register(BookIssue,BookIssueAdmin)