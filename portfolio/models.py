from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    cv = models.FileField(upload_to='cv/', blank=True, null=True) 

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(help_text="0 - 100")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class WorkExperience(models.Model):
    company = models.CharField(max_length=50)
    roles = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.roles} at {self.company}"