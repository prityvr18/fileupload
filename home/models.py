from django.db import models
from uuid import uuid4
import os
import uuid


# Create your models here.
class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now= True)
    
def get_upload_path(instance, filename):   # this function  create folder and pass a filename with uuid
    return os.path.join(str(instance.folder.uid), filename)
    
    
class Files(models.Model):
    Folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at  = models.DateField(auto_now= True)
