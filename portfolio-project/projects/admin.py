from django.contrib import admin
from .models import Home, Project, Social,Newsletter,Tag
# Register your models here.

admin.site.register(Home)
admin.site.register(Project)
admin.site.register(Social)
admin.site.register(Newsletter)
admin.site.register(Tag)

admin.site.site_header='MSD Panel'