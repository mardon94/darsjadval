from django.contrib import admin
from home.models import Faculty, Dars, Time
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

class FacultyAdmin(DraggableMPTTAdmin):
    pass
    # list_display = ['']
    list_filter = ['faculty']
    prepopulated_fields = {'slug':('faculty',)}

    # mptt_indent_field = ("faculty")
    # list_display = ('tree_actions', 'indented_faculty')
    # list_display_links = ('indented_faculty',)
    # prepopulated_fields = {'slug':('faculty',)}



class DarsAdmin(admin.ModelAdmin):
    list_display = ['yunalish', 'fan', 'teacher', 'guruh', 'time']
    list_filter = ['yunalish', 'fan', 'teacher', 'guruh', 'time']



admin.site.register(Dars, DarsAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Time)