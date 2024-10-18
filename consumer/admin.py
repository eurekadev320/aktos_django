from django.contrib import admin
from consumer.models.consumer import Consumer


@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = (
        "id", "status", "previous_jobs_count", "amount_due"
    )
