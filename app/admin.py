from django.contrib import admin
from .models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['SubjectName']
    search_fields = ['SubjectName']

class ProjectAdmin(admin.ModelAdmin):
    fields = ['ProjectName', 'Subject', 'Author' ,'Status','Users','Content', 'Summury']
    list_display = ['ProjectName', 'Subject', 'Author', 'CreatedAt', 'Status']
    list_display_links = ('ProjectName', 'Subject', 'Author', 'Status')
    list_filter = ['Subject', 'Status']
    search_fields = ['ProjectName', 'Summury']

class TaskAdmin(admin.ModelAdmin):
    list_display = ('ProjectRel', 'TaskName','DateTo', 'CreatedAt')
    list_display_links = ('ProjectRel', 'TaskName')
    list_filter = ['ProjectRel']
    search_fields = ['TaskName']

class UserProfileAdmin(admin.ModelAdmin):
    fields= ('User', 'Project')
    list_display = ['User']
    list_display_links = ['User' ]
    list_filter = ('User', 'Project')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)