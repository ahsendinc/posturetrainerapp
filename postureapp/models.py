from django.db import models
import datetime
from django.utils import timezone
from picklefield.fields import PickledObjectField
# Create your models here.

#class PostureMonitor(models.Model){
#user_Id = models.CharField(max_length = 200)

#}


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pub_date.strftime('%Y-%m-%d %H:%M:%S')
    
    def recent_published(self):
        now = timezone.now()
        return now - datetime.timedelta(minutes=2) <= self.pub_date <= now
        recent_published.admin_order_field = 'pub_date'
        recent_published.boolean = True
        recent_published.short_description = 'Recent Data'
    
    # @staticmethod
    #def recommend(self):
        
#   return True

class Recommendation(models.Model):
    repstatus = models.NullBooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)
    @classmethod
    def create(cls, repstatus):
        recommendation = cls(repstatus=repstatus)
        # do something with the recommendation
        return recommendation

class PickleObject(models.Model):
    args = PickledObjectField()
    name = models.CharField(max_length=200)
