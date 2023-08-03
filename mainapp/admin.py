from django.contrib import admin
from mainapp.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date','id')


admin.site.register(Company, CompanyAdmin)