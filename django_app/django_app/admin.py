from django.contrib import admin

from django_app.models import Company


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ["name", "age", "address", "salary", "join_date"]
    admin.register(Company)
