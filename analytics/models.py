from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User=settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user          = models.ForeignKey(User,blank=True,null=True)
    ip_address    =models.CharField(max_length=220,blank=True,null=True)
    content_type  =models.ForeignKey(ContentType)
    object_id     =models.PositiveIntegerField()
    content_object =GenericForeignKey('content_type','object_id')
    timestamp     =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s viewed on %s" %(self.content_object,self.timestamp)

    class Meta:
        ordering=['-timestamp']
        verbose_name='object_viewed'
        verbose_name_plural='objects_viewed'

# Create your models here.
