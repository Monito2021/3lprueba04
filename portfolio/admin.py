from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created','date_updated')

admin.site.register(Project, ProjectAdmin)