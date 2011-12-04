from www.models import *
from django.contrib import admin


class ProjectMemberInline(admin.TabularInline):
    model = ProjectMember


class RequisiteAdmin(admin.ModelAdmin):

    list_filter = ['project', 'requisiteType']
    list_display = ['requisiteType','number','title']
    search_fields = ['title']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['requisiteType', 'number']
        else:
            return ['number']


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectMemberInline,
    ]

    def fet_readonly_fields(self, request, obj=None):
        if obj:
            return ['repositoryPath']
        else:
            return []

admin.site.register(Project, ProjectAdmin)
admin.site.register(RequisiteType)
admin.site.register(Requisite, RequisiteAdmin)
