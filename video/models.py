from datetime import timezone
from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

def upload_location(instance, filename, **kwargs):
    file_path = 'video/{author_id}/{tancnev}-{filename}'.format(
        author_id=str(instance.author.id), tancnev=str(instance.tancnev), filename=filename
    )
    return file_path

class Post (models.Model):
    tancnev             =models.CharField(max_length=50,null=False, blank=False)
    boritokep           =models.ImageField(upload_to=upload_location, null=False, blank=False)
    slug                =models.SlugField(blank=True, unique=True)
    video               =models.FileField(upload_to=upload_location, null=False, blank=False)
    tanctipus           =models.TextField(max_length=100,null=False,blank=False,default="")
    talyegyseg          =models.TextField(max_length=100,null=False,blank=False,default="")
    fdatum              =models.DateField(blank=False,null=False,default="1950-01-01")
    adatkozlo           =models.TextField(max_length=100,null=False,blank=False,default="")
    def __str__(self):
        return self.tancnev  

@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.boritokep.delete(False)      

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.felhasznalonev + '-' + instance.tancnev)
      

pre_save.connect(pre_save_post_reciever, sender=Post)


