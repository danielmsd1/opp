from django.db import models

# Create your models here.
class Home(models.Model):
	home_text = models.TextField()
	github_link = models.URLField()
	email = models.EmailField()

	def __str__(self) -> str:
		return self.home_text


class Project(models.Model):
	image_link = models.URLField()
	title = models.CharField(max_length=200)
	description = models.TextField()
	client = models.CharField(max_length=200)
	playstore = models.URLField(null=True,blank=True)
	website = models.URLField(null=True,blank=True)
	github = models.URLField(null=True,blank=True)
	medium = models.URLField(null=True,blank=True)

	def __str__(self) -> str:
		return self.title

class Social(models.Model):
	instagram = models.URLField()
	twitter = models.URLField()
	medium = models.URLField()
	linkedin = models.URLField()

class Tag(models.Model):
	title = models.CharField(max_length=200)

class Newsletter(models.Model):
	heading = models.TextField()