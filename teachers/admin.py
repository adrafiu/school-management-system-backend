from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "subject",
        "experience_years",
        "is_active",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "subject",
    )

    list_filter = (
        "subject",
        "is_active",
    )

    list_per_page = 10
