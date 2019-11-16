from django.contrib import admin
from projects.models import Project


admin.site.register(Project)


#class ProjectAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Project, ProjectAdmin)
