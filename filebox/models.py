from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class File(models.Model):
    about=models.CharField(max_length=100)
    file=models.FileField(upload_to='shared_files')
    date_uploaded=models.DateTimeField(default=timezone.now)
    uploaded_by=models.ForeignKey(User, on_delete=models.CASCADE)
    objects=models.Manager() 
    
    def __str__(self):
        return self.about
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})