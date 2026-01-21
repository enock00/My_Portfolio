from django.contrib import admin
from .models import Profile, Skill, Project, ContactMessage, WorkExperience

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactMessage)
admin.site.register(WorkExperience)

