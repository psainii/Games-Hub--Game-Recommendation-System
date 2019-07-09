from django.db import models
from django.contrib.auth.models import User
class launch(models.Model):
	name=models.CharField(max_length=50,primary_key=True)
	company=models.CharField(max_length=100)
	year=models.IntegerField()
	class Meta:
		ordering=("-year",)
	def __str__(self):
		return str(self.name)
class popular(models.Model):
	name=models.ForeignKey(launch,on_delete=models.CASCADE,unique=True)
	votes=models.IntegerField()
	class Meta:
		ordering=("-votes",)
	def get_absolute_url(self):
		return "/games/%s" % self.name
	def __str__(self):
		return str(self.name)
class description(models.Model):
	name=models.ForeignKey(launch,on_delete=models.CASCADE,unique=True)
	description=models.CharField(max_length=10000)
	def __str__(self):
		return str(self.name)
class genres(models.Model):
	l1=(('arcade','arcade'),('action','action'),('racing','racing'),('puzzle','puzzle'),('strategy','strategy'),('sports','sports'),('war','war'),)
	name=models.ForeignKey(launch,on_delete=models.CASCADE,unique=True)
	genre=models.CharField(max_length=20,choices=l1)
	def __str__(self):
		return str(self.name)
class logo(models.Model):
	name=models.ForeignKey(launch,on_delete=models.CASCADE,unique=True)
	link=models.CharField(max_length=1000)
	def __str__(self):
		return str(self.name)
class response(models.Model):
	name=models.CharField(max_length=100)
	phoneno=models.IntegerField()
	email=models.CharField(max_length=100)
	message=models.CharField(max_length=1000)




