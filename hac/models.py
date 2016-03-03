from django.db import models
from django.utils import timezone
import datetime
from django.core import serializers
from django.contrib import admin

class Attendee(models.Model):
	name = models.CharField(max_length=200)
	corpId = models.CharField(max_length=200)
	app_version = models.CharField(max_length=200)
	device_type = models.CharField(max_length=200)

	ibeacon_uuid = models.CharField(max_length=200)
	major_id = models.CharField(max_length=200)
	minor_id = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.name

#@admin.register(Attendee)
#class AttendeeAdmin(admin.ModelAdmin):
#	list_display = ('corpId') 

class Speaker(models.Model):
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	imageUrl = models.CharField(max_length=40, default=None,blank=True, null=True)
	bio = models.TextField(default=None,blank=True, null=True)

	def asjson(self):
		return "{" + "\"name\" : \"" + self.name + "\"," + "\"title\":\"" + self.title + "\"," + "\"imageUrl\":\"" + self.imageUrl + "\","  + "\"bio\":\"" + self.bio + "\""+ "}"  
		
	def __str__(self):
		return self.name

class Floor(models.Model):
	name = models.CharField(max_length=200)
	def asjson(self):
		return "," + "\"floor\" : \"" + self.name + "\""+ "" 
	def __str__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=200)
	floor = models.ForeignKey(Floor, default=None, null=True, blank=True)
	def asjson(self):
		return self.floor.asjson() + "," + "\"location\" : \"" + self.name + "\""+ "" 
	def __str__(self):
		return self.name

class Timeslot(models.Model):
	name = models.CharField(max_length=200)
	def asjson(self):
		return "," + "\"timeslot\" : \"" + self.name + "\""+ "" 
	def __str__(self):
		return self.name

class Beacon(models.Model):
	major = models.CharField(max_length=200)
	minor = models.CharField(max_length=200)
	macAddress = models.CharField(max_length=200, blank=True)
	uuid = models.CharField(max_length=200, blank=True)
	location = models.ForeignKey(Location)

	def asjson(self):
		return "{" + "\"macAddress\" : \"" + self.macAddress + "\"," + "\"major\" : \"" + self.major + "\"," + "\"minor\":\"" + self.minor + "\""  + self.location.asjson() + "}"  
		
	def __str__(self):
		return self.location.name + " " + self.major + " " + self.minor

class Session(models.Model):
	speaker = models.ForeignKey(Speaker, related_name='speaker1')
	speaker2 = models.ForeignKey(Speaker, related_name='speaker2', default=None, null=True, blank=True)
	title = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
	timeslot = models.ForeignKey(Timeslot)
	details = models.TextField(default=None, null=True, blank=True)

	created_date = models.DateTimeField(
			default=timezone.now)
	date = models.DateTimeField(default=datetime.datetime(2016, 5, 3, 0, 0),
			blank=True, null=True)

	def asjson(self):
		return "{ \"eventName\" : \"" + self.title + "\"," + "\"description\" : \"" + self.details + "\"," + "\"date\" : \"" + self.date.strftime('%d-%m-%Y') + "\"" + self.location.asjson() + self.timeslot.asjson() + "," + "\"speaker\" : " + self.speaker.asjson() + "}"
		# + self.location.asjson() + self.timeslot.asjson + "}"

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
