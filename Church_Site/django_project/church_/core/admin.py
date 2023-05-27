import csv
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Email

def export_users_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="usuarios.csv"'

    writer = csv.writer(response)
    writer.writerow(['Email', 'Nome', 'Sobrenome'])

    for user in queryset:
        writer.writerow([user.email, user.nome, user.sobrenome])

    total_users = queryset.count()
    writer.writerow([])
    writer.writerow(['Total de Usuários: ', total_users])

    return response

export_users_to_csv.short_description = 'Exportar usuários para CSV'

class EmailAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    list_filter = ('nome', 'sobrenome',)
    actions = [export_users_to_csv]

admin.site.register(Email, EmailAdmin)
