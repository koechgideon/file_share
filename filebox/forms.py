from django import forms
from filebox.models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields=('about','shared_file','date_uploaded','uploaded_by')