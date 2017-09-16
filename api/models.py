from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

# Create your models here.

class Household(models.Model):
    HID = models.AutoField(primary_key=True)
    income = models.IntegerField(default=0)
    point = models.PointField(default=Point(1,1),null=True)
    def __str__(self):
        return "%s" %(self.HID)

class Member(models.Model):
    PID = models.AutoField(primary_key=True)
    HID = models.ForeignKey(Household,to_field='HID',on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    genders = (('M',"Male"),('F',"Female"))
    name = models.CharField(max_length=30,default="")
    gender = models.CharField(max_length=1,choices=genders)
    def __str__(self):
        return "%s : %s" %(self.PID,self.name)

class Farm(models.Model):
    FID = models.AutoField(primary_key=True)
    HID = models.ForeignKey(Household,to_field='HID',on_delete=models.CASCADE)
    plot = models.PolygonField(srid=4326,geography=True)
    area = models.FloatField(default=0.0)
    def __str__(self):
        return "%s" % (self.FID)
    def save(self):
        temp=self.plot.transform(27700,clone=True)
        self.area=temp.area
        super().save(self)

class Well(models.Model):
    WID = models.AutoField(primary_key=True)
    HID = models.ForeignKey(Household,to_field='HID',on_delete=models.CASCADE)
    point = models.PointField(default=Point(1,1),null=True)
    AvgYield=models.DecimalField(max_digits=7,decimal_places=4)
    def __str__(self):
        return "%s" %(self.WID)

class Yield(models.Model):
    WID = models.ForeignKey(Well,to_field='WID',on_delete=models.CASCADE)
    yields = models.FloatField(default=0.0)
    measured_date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return "%s : %s" %(self.WID,self.measured_date)

class Crop(models.Model):
    Name = models.CharField(max_length=50,default="Rice")
    FID = models.ForeignKey(Farm,to_field='FID',on_delete=models.CASCADE)
    Year = models.IntegerField()
    seasons = (('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
    season = models.CharField(max_length=20,choices=seasons)
    def __str__(self):
        return "%s : %s" %(self.FID,self.Year)