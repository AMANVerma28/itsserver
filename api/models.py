from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime
# Create your models here.

class Household(models.Model):
    HID = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=30)
    number_of_member = models.IntegerField(null = True,blank = False)
    location = models.PointField(default=Point(1,1),null=True)
    monthly_income = models.IntegerField(null = True,blank = False)
    image = models.FileField(upload_to = 'HouseHold_photo')
    video = models.FileField(upload_to = 'HouseHold_video')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.HID, self.owner_name)

class Farm(models.Model):
    HID = models.ForeignKey(Household,to_field='HID',on_delete=models.CASCADE)
    FID = models.AutoField(primary_key=True)
    plot = models.PolygonField(srid=4326,geography=True)
    area = models.FloatField(default=0.0)
    image = models.FileField(upload_to = 'Farm_photo')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.HID, self.FID)
    def save(self):
        temp=self.plot.transform(27700,clone=True)
        self.area=temp.area
        super().save(self)

class Storage(models.Model):
    SID = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=30)
    location = models.PointField(default=Point(1,1),null=True)
    capacity = models.FloatField(null = True,blank = False)
    image = models.FileField(upload_to = 'Storage_photo')
    def __str__(self):
        return "%s : %s" % (self.SID, self.owner_name)

class Season(models.Model):
    seasons = (('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
    season = models.CharField(max_length=20,choices=seasons)
    def __str__(self):
        return "%s" %(self.season)

class Crop(models.Model):
    Crop = models.CharField(max_length=50)
    FID = models.ForeignKey(Farm,to_field='FID',on_delete=models.CASCADE)
    season = models.ForeignKey(Season,on_delete = models.CASCADE)
    Yield= models.FloatField(null = True,blank = False)
    Extent = models.FloatField(null = True,blank = False)
    year = models.IntegerField(null = True, blank = False)
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s-%s" %(self.FID,self.year,self.season)

class Well(models.Model):
    WID = models.AutoField(primary_key=True)
    FID = models.ForeignKey(Farm,to_field='FID',on_delete=models.CASCADE)
    location = models.PointField(default=Point(1,1),null=True)
    average_yield = models.DecimalField(max_digits=7,decimal_places=4)
    depth = models.FloatField(null = True,blank = False)
    image = models.FileField(upload_to = 'Well_photo')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s" %(self.WID)

class Yield(models.Model):
    WID = models.ForeignKey(Well,to_field='WID',on_delete=models.CASCADE)
    Yield = models.FloatField(default=0.0)
    Time = models.DateTimeField(auto_now_add = True, blank = False)
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" %(self.WID,self.DateTime)

class Member(models.Model):
    HID = models.ForeignKey(Household, to_field='HID', on_delete = models.CASCADE)
    name = models.CharField(null = True,blank = False,max_length = 50)
    relation = models.CharField(null = True,blank = False,max_length = 50)
    age = models.IntegerField(null = True,blank = False)
    image = models.FileField(upload_to = 'Member_photo')
    audio = models.FileField(upload_to = 'Member_audio')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" %(self.HID, self.name)

"""
class Household_Photo(models.Model):
    HID = models.ForeignKey(Household, to_field='HID', on_delete = models.CASCADE)
    HPID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'HouseHold_photo')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.HPID, self.DateTime)

class Farm_Photo(models.Model):
    FID = models.ForeignKey(Farm,to_field='FID',on_delete=models.CASCADE)
    FPID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'Farm_photo')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.FPID, self.DateTime)

class Well_Photo(models.Model):
    WID = models.ForeignKey(Well,to_field='WID',on_delete=models.CASCADE)
    WPID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'Well_photo')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.WPID, self.DateTime)

class Storage_Photo(models.Model):
    SID = models.ForeignKey(Storage,to_field='SID',on_delete=models.CASCADE)
    SPID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'Storage_photo')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.SPID, self.DateTime)

class Household_Audio(models.Model):
    HID = models.ForeignKey(Household, to_field='HID', on_delete = models.CASCADE)
    HAID = models.AutoField(primary_key=True)
    audio = models.FileField(upload_to = 'HouseHold_audio')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.HAID, self.DateTime)

class Household_Video(models.Model):
    HID = models.ForeignKey(Household, to_field='HID', on_delete = models.CASCADE)
    HVID = models.AutoField(primary_key=True)
    vudio = models.FileField(upload_to = 'HouseHold_video')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.HVID, self.DateTime)

class Farm_Video(models.Model):
    FID = models.ForeignKey(Farm,to_field='FID',on_delete=models.CASCADE)
    FVID = models.AutoField(primary_key=True)
    audio = models.FileField(upload_to = 'Farm_video')
    DateTime= models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s : %s" % (self.FVID, self.DateTime)
        """