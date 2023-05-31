import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Email

# Register your models here.
def Import_To_Csv(modeladmin,request, queryset):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename="user.csv'

    writer = csv.writer(response)
    writer.writerow(['nome','congregacao','email'])
    
    for user in queryset:
        writer.writerow([user.nome,user.congregacao,user.email])
        
    total_users = queryset.count()
    writer.writerow([])
    writer.writerow(['Total de Inscritos: ', total_users])
    
    return response


class EmailAdmin(admin.ModelAdmin):
    list_display = ('nome','congregacao','email')
    list_filter = ('nome','congregacao','email')
    actions = [Import_To_Csv]
    
admin.site.register(Email,EmailAdmin)